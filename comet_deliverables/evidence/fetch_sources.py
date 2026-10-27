import urllib.request, concurrent.futures, json, re, html
from pathlib import Path
BASE=Path(__file__).parent
sources={
'S01':'https://arxiv.org/abs/1705.07874',
'S02':'https://arxiv.org/abs/1602.04938',
'S03':'https://arxiv.org/abs/2202.01602',
'S04':'https://arxiv.org/abs/2106.12228',
'S05':'https://arxiv.org/abs/1903.10464',
'S06':'https://arxiv.org/abs/2006.16234',
'S07':'https://arxiv.org/abs/1903.00519',
'S08':'https://www.ijcai.org/Proceedings/2020/417',
'S09':'https://arxiv.org/abs/1909.09223',
'S10':'https://www.nature.com/articles/s42256-019-0048-x',
'S11':'https://proceedings.mlr.press/v162/dutta22a.html',
'S12':'https://arxiv.org/abs/2203.06768',
'S13':'https://arxiv.org/abs/2012.11788',
'S14':'https://arxiv.org/abs/2102.13620',
'S15':'https://arxiv.org/abs/1905.07697',
'S16':'https://arxiv.org/abs/2002.06278',
'S17':'https://arxiv.org/abs/2211.13358',
'S18':'https://proceedings.mlr.press/v266/maalej25a.html',
'S19':'https://arxiv.org/abs/2609.39877',
'S20':'https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients',
'S21':'https://github.com/fico-xai/heloc-dataset',
'S22':'https://shap.readthedocs.io/en/latest/generated/shap.TreeExplainer.html',
'S23':'https://shap.readthedocs.io/en/latest/generated/shap.PartitionExplainer.html',
'S24':'https://interpret.ml/docs/python/api/ExplainableBoostingClassifier.html',
'S25':'https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html',
'S26':'https://numpy.org/doc/stable/reference/generated/numpy.quantile.html',
'S27':'https://www.jmlr.org/papers/v7/demsar06a.html',
'S28':'https://www.consumerfinance.gov/rules-policy/regulations/1002/9/',
'S29':'https://www.consumerfinance.gov/rules-policy/regulations/1002/6/',
'S30':'https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng',
'S31':'https://www.law.cornell.edu/uscode/text/15/1681g',
'S32':'https://arxiv.org/abs/1811.12615',
'S33':'https://arxiv.org/abs/1802.03888',
'S34':'https://arxiv.org/abs/1711.00399',
'S35':'https://www.ijcai.org/proceedings/2019/388',
'S36':'https://arxiv.org/abs/1810.03292',
'S37':'https://arxiv.org/abs/1905.03151',
'S38':'https://arxiv.org/abs/2011.13951',
'S39':'https://arxiv.org/abs/1911.02508',
'S40':'https://arxiv.org/abs/2302.01332',
}
def fetch(item):
 k,u=item
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (academic literature verification)'})
  with urllib.request.urlopen(req,timeout=40) as r: raw=r.read().decode(errors='replace');status=r.status;final=r.url
  (BASE/(k+'.html')).write_text(raw)
  titles=re.findall(r'<meta\s+name="citation_title"\s+content="(.*?)"',raw)
  authors=re.findall(r'<meta\s+name="citation_author"\s+content="(.*?)"',raw)
  if not titles: titles=re.findall(r'<title[^>]*>(.*?)</title>',raw,re.S)
  a=re.findall(r'<blockquote class="abstract[^>]*>(.*?)</blockquote>',raw,re.S)
  clean=re.sub(r'<(script|style)\b[^>]*>.*?</\1>','',raw,flags=re.S)
  clean=html.unescape(re.sub('<[^>]+>',' ',clean));clean=re.sub(r'\s+',' ',clean)
  (BASE/(k+'.txt')).write_text(clean)
  return {'id':k,'url':u,'status':status,'title':html.unescape(titles[0]).strip() if titles else '', 'authors':authors,'abstract':html.unescape(re.sub('<[^>]+>',' ',a[0])).strip() if a else '', 'final_url':final}
 except Exception as e:return {'id':k,'url':u,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex: results=list(ex.map(fetch,sources.items()))
(BASE/'sources.json').write_text(json.dumps(results,indent=2))
for r in results: print(r['id'],r.get('status',r.get('error')),r.get('title',''))
