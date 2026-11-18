#!/usr/bin/env python3
"""Independent numerical audit for the finite MCC 3.0 toy. Python + numpy."""
import json,hashlib
import numpy as np
import mcc3_local_toy_v08 as m
def audit():
    f=m.source();phi=m.metric(f); original=m.run();ledger=f.sum(axis=1)
    n=len(phi)
    local=.5*(f[1]/ledger[1]+f[2]/ledger[2]);local-=local.mean()
    k=2*np.pi*np.fft.rfftfreq(n,d=1/n)
    lap=np.fft.irfft(-k*k*np.fft.rfft(phi),n=n)
    coefficient=float(np.dot(lap,local)/np.dot(local,local))
    l2=float(np.linalg.norm(lap-coefficient*local)/np.linalg.norm(lap))
    q=5*49*np.sqrt(1-2*phi)/(1+49*np.sqrt(1-2*phi))
    checks={
      'original 12':original['passed']==12 and original['total']==12,
      'independent Fourier L2 residual':l2<1e-10,
      'address ledger':bool(np.allclose(ledger,[.05,.268,.682],rtol=0,atol=3e-12)),
      'nonnegative bins':bool(np.all(f>=-1e-16)),
      'zero potential mean':abs(float(phi.mean()))<1e-18,
      'weak metric':float(np.max(abs(phi)))<=1.0000001e-8,
      'nontrivial local q':float(np.ptp(q))>0,
      'bounded q':bool(np.all((q>0)&(q<5))),
      'proper circumference':abs(original['outputs'][3]['proper_ring_length']-1)<1e-13,
      'today q':abs(original['outputs'][3]['q_eff']-4.9)<1e-12,
      'deterministic':json.dumps(m.run(),sort_keys=True)==json.dumps(m.run(),sort_keys=True),
      'declared amplitude':original['inputs']['metric_amplitude']==1e-8
    }
    return {'passed':int(sum(checks.values())),'total':len(checks),'tests':{k:bool(v) for k,v in checks.items()},
            'poisson_l2_relative':l2,'poisson_coefficient':coefficient,
            'local_q_range':[float(q.min()),float(q.max())],
            'address_bins':f.tolist(),'metric_phi':phi.tolist(),'original':original}
if __name__=='__main__':
    result=audit()
    with open('audit_full.json','w') as fp:json.dump(result,fp,indent=2)
    print(result['passed'],'/',result['total'])
    assert result['passed']==result['total']
