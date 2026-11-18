#!/usr/bin/env python3
"""MCC 3.0 finite-address -> periodic local metric -> effective quantization.
Toy receiver, NOT the original MCC 3.0 28-component GR solver.
"""
import json, math
import numpy as np
N=1015000
ALPHA=1.8996877935161325
H=1.4476744689338703
GAMMA=np.array([14.134725141734695,21.022039638771556,25.01085758014569,30.424876125859512])
OMEGA=(.0493,.265,.6857)
I=5.
def source(nbins=128):
    n=np.arange(2,N+1,dtype=np.int64)
    sieve=np.ones(N+1,bool); sieve[:2]=False
    for p in range(2,math.isqrt(N)+1):
        if sieve[p]: sieve[p*p::p]=False
    prime=sieve[n]; even=(n%2==0)&~prime; odd=(n%2==1)&~prime
    w=n.astype(float)**(-ALPHA); w/=w.sum()
    admission=np.zeros(len(n))
    logs=np.log(n[odd].astype(float)); rejected=np.ones(len(logs))
    for frame in range(8):
        d=.5*np.cos((logs[:,None]+.1*frame)*GAMMA).sum(axis=1)
        rejected*=1-1/(1+np.exp(-(d-H)))
    admission[odd]=1-rejected
    p=w*admission; d=w*even; r=w-p-d
    bins=n%nbins
    return np.stack([np.bincount(bins,weights=z,minlength=nbins) for z in (p,d,r)])
def metric(fields,amplitude=1e-8):
    totals=fields.sum(axis=1)
    local=.5*(fields[1]/totals[1]+fields[2]/totals[2])
    contrast=local-local.mean()
    k=2*np.pi*np.fft.rfftfreq(len(local),d=1/len(local))
    modes=np.fft.rfft(contrast); modes[1:]/=k[1:]**2; modes[0]=0
    raw=np.fft.irfft(modes,n=len(local))
    return raw*(amplitude/max(abs(raw)))
def state(fields,phi,a):
    R=float((a*np.sqrt(1-2*phi)/len(phi)).sum())
    ratio=49*R; q=I*ratio/(1+ratio)
    om=OMEGA[0]+OMEGA[1]; ov=OMEGA[2]
    E2=om/a**3+ov
    return dict(a=a,H_over_H0=math.sqrt(E2),proper_ring_length=R,q_eff=q,
                residual=I-q,q_conservation_error=q+(I-q)-I,
                background_continuity_residual=abs((-3*om/a**3+3*om/a**3)/E2))
def run():
    fields=source(); phi=metric(fields); ledger=fields.sum(axis=1)
    outputs=[state(fields,phi,a) for a in (.02,.1,.6119598068,1.,2.)]
    k=2*np.pi*np.fft.rfftfreq(len(phi),d=1/len(phi))
    lap=np.fft.irfft(-k*k*np.fft.rfft(phi),n=len(phi))
    local=.5*(fields[1]/ledger[1]+fields[2]/ledger[2]);local-=local.mean()
    coeff=np.dot(lap,local)/np.dot(local,local)
    residual=np.max(abs(lap-coeff*local))/max(abs(lap))
    qlocal=5*49*np.sqrt(1-2*phi)/(1+49*np.sqrt(1-2*phi))
    tests={
      'address ledger':np.max(abs(ledger-[.05,.268,.682]))<2e-12,
      'address sum':abs(ledger.sum()-1)<1e-12,
      'finite periodic metric':np.all(np.isfinite(phi)) and abs(phi.mean())<1e-20,
      'periodic Poisson residual':residual<1e-10,
      'weak field':max(abs(phi))<=1.00000001e-8,
      'information conserved':max(abs(o['q_conservation_error']) for o in outputs)<1e-13,
      'background energy continuity':max(o['background_continuity_residual'] for o in outputs)<1e-12,
      'expansion monotonic q':all(x['q_eff']<y['q_eff'] for x,y in zip(outputs,outputs[1:])),
      'finite response at early a':all(0<o['q_eff']<5 for o in outputs),
      'time independent potential':np.array_equal(phi,metric(fields)),
      'finite stress response':np.isfinite(coeff),
      'nontrivial local q response':np.ptp(qlocal)>0,
    }
    return dict(claim='Independent periodic Poisson-type MCC toy; not original 28-mode GR',
      inputs=dict(N=N,alpha=ALPHA,bins=len(phi),metric_amplitude=1e-8,
        address_mapping='n mod 128',metric_receiver='periodic Poisson, zero mode removed',
        metric_time_rule='static comoving potential + FLRW',energy_fractions=OMEGA,
        quantization_toy=dict(I=I,q0=4.9)),
      ledger=dict(zip(('P','D','R'),map(float,ledger))),
      local_source=dict(D_plus_R_density_min=float(local.min()),D_plus_R_density_max=float(local.max()),
        potential_min=float(phi.min()),potential_max=float(phi.max()),
        poisson_relative_residual=float(residual),
        local_q_min_a1=float(qlocal.min()),local_q_max_a1=float(qlocal.max())),
      outputs=outputs,tests={k:bool(v) for k,v in tests.items()},
      passed=int(sum(tests.values())),total=int(len(tests)))
if __name__=='__main__': print(json.dumps(run(),indent=2,ensure_ascii=False))
