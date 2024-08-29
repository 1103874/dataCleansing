
import numpy as np
import soundfile as sf
import pyttsx3

# pyttsx3 엔진 초기화
engine = pyttsx3.init()

# 첫 번째 문장 읽기 및 저장
engine.save_to_file('TBM 일단계, 개인의 건강상태 확인 및 보호구 확인.', './utils/part1.mp3')
engine.say('TBM 일단계, 개인의 건강상태 확인 및 보호구 확인.')
engine.runAndWait()

# 두 번째 문장 읽기 및 저장
engine.save_to_file('작업자의 건강상태와 개인보호구의 적합상태를 확인합니다.', './utils/part2.mp3')
engine.say('작업자의 건강상태와 개인보호구의 적합상태를 확인합니다.')
engine.runAndWait()

# 세 번째 문장 읽기 및 저장
# engine.save_to_file('세 번째 문장 내용', './utils/part3.mp3')
# engine.runAndWait()

# 오디오 파일 로드
part1, samplerate = sf.read('./utils/part1.mp3')
part2, _ = sf.read('./utils/part2.mp3')
# part3, _ = sf.read('./utils/part3.mp3')

# 일시적인 중지를 위한 공백 생성 (1초)
pause = np.zeros(samplerate)

# 오디오 파일 합치기
final = np.concatenate((part1, pause, part2, pause))
# final = np.concatenate((part1, pause, part2, pause, part3))

# 최종 오디오 파일 저장
sf.write('./utils/tbm_voice_1.mp3', final, samplerate)






import numpy as np
import soundfile as sf
import pyttsx3

# pyttsx3 엔진 초기화
engine = pyttsx3.init()

# 첫 번째 문장 읽기 및 저장
engine.save_to_file('TBM 일단계, 개인의 건강상태 확인 및 보호구 확인.', './utils/part1.mp3')
engine.say('TBM 일단계, 개인의 건강상태 확인 및 보호구 확인.')
engine.runAndWait()

# 두 번째 문장 읽기 및 저장
engine.save_to_file('작업자의 건강상태와 개인보호구의 적합상태를 확인합니다.', './utils/part2.mp3')
engine.say('작업자의 건강상태와 개인보호구의 적합상태를 확인합니다.')
engine.runAndWait()

# 세 번째 문장 읽기 및 저장
# engine.save_to_file('세 번째 문장 내용', './utils/part3.mp3')
# engine.runAndWait()

# 오디오 파일 로드
part1, samplerate = sf.read('./utils/part1.mp3')
part2, _ = sf.read('./utils/part2.mp3')
# part3, _ = sf.read('./utils/part3.mp3')

# 일시적인 중지를 위한 공백 생성 (1초)
pause = np.zeros(samplerate)

# 오디오 파일 합치기
final = np.concatenate((part1, pause, part2, pause))
# final = np.concatenate((part1, pause, part2, pause, part3))

# 최종 오디오 파일 저장
sf.write('./utils/tbm_voice_1.mp3', final, samplerate)



import numpy as np
import soundfile as sf
import pyttsx3

# pyttsx3 엔진 초기화
engine = pyttsx3.init()

# 첫 번째 문장 읽기 및 저장
engine.save_to_file('TBM 삼단계, 작업자의 숙지여부 확인.', './utils/part1.mp3')
engine.say('TBM 삼단계, 작업자의 숙지여부 확인.')
engine.runAndWait()

# 두 번째 문장 읽기 및 저장
engine.save_to_file('작업자 공유 그리고 교육 사항 숙지 여부를 확인합니다.', './utils/part2.mp3')
engine.say('작업자 공유 그리고 교육 사항 숙지 여부를 확인합니다.')
engine.runAndWait()

# 세 번째 문장 읽기 및 저장
engine.save_to_file('위험요인, 불안전상태 발견 시 행동요령을 확인합니다.', './utils/part3.mp3')
engine.say('위험요인, 불안전상태 발견 시 행동요령을 확인합니다.')
engine.runAndWait()

# 네 번째 문장 읽기 및 저장
engine.save_to_file('작업자의 불만, 질문, 제안사항을 확인합니다.', './utils/part4.mp3')
engine.say('작업자의 불만, 질문, 제안사항을 확인합니다.')
engine.runAndWait()

# 오디오 파일 로드
part1, samplerate = sf.read('./utils/part1.mp3')
part2, _ = sf.read('./utils/part2.mp3')
part3, _ = sf.read('./utils/part3.mp3')
part4, _ = sf.read('./utils/part4.mp3')

# 일시적인 중지를 위한 공백 생성 (1초)
pause = np.zeros(samplerate)

# 오디오 파일 합치기
# final = np.concatenate((part1, pause, part2, pause))
# final = np.concatenate((part1, pause, part2, pause, part3))
final = np.concatenate((part1, pause, part2, pause, part3, pause, part4))

# 최종 오디오 파일 저장
sf.write('./utils/tbm_voice_3.mp3', final, samplerate)







import numpy as np
import soundfile as sf
import pyttsx3

# pyttsx3 엔진 초기화
engine = pyttsx3.init()

# 첫 번째 문장 읽기 및 저장
engine.save_to_file('TBM 사단계, TBM 결과 확인.', './utils/part1.mp3')
engine.say('TBM 사단계, TBM 결과 확인.')
engine.runAndWait()

# 두 번째 문장 읽기 및 저장
engine.save_to_file('시스템에 입력한 TBM 활동 결과를 최종 확인합니다.', './utils/part2.mp3')
engine.say('시스템에 입력한 TBM 활동 결과를 최종 확인합니다.')
engine.runAndWait()

# 세 번째 문장 읽기 및 저장
# engine.save_to_file('위험요인, 불안전상태 발견 시 행동요령을 확인합니다.', './utils/part3.mp3')
# engine.say('위험요인, 불안전상태 발견 시 행동요령을 확인합니다.')
# engine.runAndWait()

# 네 번째 문장 읽기 및 저장
# engine.save_to_file('작업자의 불만, 질문, 제안사항을 확인합니다.', './utils/part4.mp3')
# engine.say('작업자의 불만, 질문, 제안사항을 확인합니다.')
# engine.runAndWait()

# 오디오 파일 로드
part1, samplerate = sf.read('./utils/part1.mp3')
part2, _ = sf.read('./utils/part2.mp3')
# part3, _ = sf.read('./utils/part3.mp3')
# part4, _ = sf.read('./utils/part4.mp3')

# 일시적인 중지를 위한 공백 생성 (1초)
pause = np.zeros(samplerate)

# 오디오 파일 합치기
final = np.concatenate((part1, pause, part2, pause))
# final = np.concatenate((part1, pause, part2, pause, part3))
# final = np.concatenate((part1, pause, part2, pause, part3, pause, part4))

# 최종 오디오 파일 저장
sf.write('./utils/tbm_voice_4.mp3', final, samplerate)