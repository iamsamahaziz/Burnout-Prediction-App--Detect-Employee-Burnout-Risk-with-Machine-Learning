import urllib.request, urllib.parse, re, time

url = 'http://localhost:5000/predict'
tests = [
    ('HIGH RISK    (stress=9, hours=70, sat=1.5)', {'age':'25','experience':'2','gender':'Male','work_hours':'70','remote_ratio':'10','stress':'9','satisfaction':'1.5','job_role':'Engineer'}),
    ('LOW RISK     (stress=2, hours=35, sat=4.5)', {'age':'35','experience':'10','gender':'Female','work_hours':'35','remote_ratio':'80','stress':'2','satisfaction':'4.5','job_role':'Analyst'}),
    ('MEDIUM RISK  (stress=6, hours=50, sat=2.8)', {'age':'30','experience':'5','gender':'Male','work_hours':'50','remote_ratio':'40','stress':'6','satisfaction':'2.8','job_role':'Manager'}),
    ('EXTREME      (stress=10, hours=90, sat=1.0)', {'age':'22','experience':'1','gender':'Male','work_hours':'90','remote_ratio':'0','stress':'10','satisfaction':'1.0','job_role':'Sales'}),
    ('RELAXED      (stress=1, hours=30, sat=5.0)', {'age':'40','experience':'15','gender':'Female','work_hours':'30','remote_ratio':'90','stress':'1','satisfaction':'5.0','job_role':'HR'}),
]

print('='*55)
print('  BURNOUT PREDICTION TEST RESULTS')
print('='*55)
for name, data in tests:
    encoded = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(url, data=encoded)
    resp = urllib.request.urlopen(req)
    html = resp.read().decode()
    match = re.search(r'data-target="([\d.]+)"', html)
    if match:
        score = float(match.group(1))
        print(f'  {name}')
        print(f'    -> Score: {score}%')
        print()
    time.sleep(0.5)

print('='*55)
print('  Scores should go: HIGH > MEDIUM > LOW')
print('  EXTREME should be highest, RELAXED lowest')
