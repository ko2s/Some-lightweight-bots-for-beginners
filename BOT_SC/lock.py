candidates1 = {
    'عقيله الوصارة': {'name': 'عقيله الوصارة', 'votes': 1, 'section': 'مسابقة أفضل تطبيق'},
    'احمد فرج': {'name': 'احمد فرج', 'votes': 0, 'section': 'مسابقة أفضل تطبيق'},
    'فرج الكيلاني': {'name': 'فرج الكيلاني', 'votes': 0, 'section': 'مسابقة أفضل تطبيق'},
    'احمد سالم': {'name': 'احمد سالم', 'votes': 0, 'section': 'مسابقة افضل مشروع AI'}
}

ntejt = {}

# التمرير على المتسابقين وجمع بياناتهم حسب القسم (المسابقة)
for ke, va in candidates1.items():
    name = va['name']      # اسم المتسابق
    vod = va['votes']      # عدد الأصوات
    sec = va['section']    # اسم المسابقة
    
    # إذا كانت المسابقة غير موجودة بعد، نقوم بإضافتها كقاموس فارغ
    if sec not in ntejt:
        ntejt[sec] = []
    
    # إضافة المتسابق وأصواته إلى المسابقة
    ntejt[sec].append({'name': name, 'votes': vod})

# طباعة النتائج مع التعامل مع حالات التعادل والفوز
for sec, participants in ntejt.items():
    # إيجاد أعلى عدد من الأصوات في المسابقة
    max_votes = max(participant['votes'] for participant in participants)
    
    # جمع المتسابقين الذين حصلوا على أعلى عدد من الأصوات
    winners = [participant['name'] for participant in participants if participant['votes'] == max_votes]
    
    # التحقق من وجود تعادل أو فائز واحد
    if len(winners) > 1:
        # حالة التعادل
        winners_text = ', '.join([f"{name} 🗳️ بعدد أصوات: {max_votes}" for name in winners])
        print(f"🔔 النتيجة هي تعادل بين المتسابقين في {sec}:\n\n{winners_text}")
    else:
        # حالة فوز متسابق واحد
        print(f"🎉 الفائز في {sec} هو: {winners[0]} 🏆 بعدد أصوات: {max_votes}")

#print(ntejt)
