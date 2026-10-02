# 내 주식 히트맵 (폰에서 쓰기)

## 처음 한 번만 하는 설정 (약 10분)
1. github.com 에서 **New repository** → 이름 예: `stock-heatmap`, **Public** 선택 → Create.
2. 저장소 화면에서 **uploading an existing file** 을 눌러, 이 폴더 안의 파일 전부(`.github` 폴더 포함)를 끌어다 놓고 **Commit changes**.
   - `.github` 폴더가 안 올라가면: **Add file → Create new file** → 파일 이름 칸에 `.github/workflows/update-prices.yml` 입력 → 이 파일 내용을 붙여넣고 Commit.
3. **Settings → Pages** → Branch: `main`, 폴더 `/ (root)` → Save. 1~2분 뒤 `https://내아이디.github.io/stock-heatmap/` 주소가 생겨요.
4. **Actions 탭** → `update-prices` → **Run workflow** 한 번 실행. 초록 체크가 뜨고 `prices.json` 의 날짜가 바뀌면 성공.
5. 폰에서 3번의 주소를 열고 홈 화면에 추가. 이 주소로 열어야 종가가 자동으로 들어와요.

## 평소 사용
- 폰 캡처를 [캡처 읽기]에 올리면 끝. 종가는 평일 한국시간 약 16:30 이후 자동 갱신돼요.
- 새 종목을 샀다면: 앱 [종목 관리] → **보유 종목코드 복사** → 저장소의 `codes.json` 편집(연필 아이콘)에서 내용 교체 → Commit. 다음 갱신부터 그 종목 종가가 들어와요.
- 데이터(계좌·수량)는 쓰는 기기의 브라우저에만 저장돼요. 폰에서만 쓰면 폰에만 있어요. 기기를 바꿀 땐 [백업 내려받기/불러오기].

## 알아둘 점
- 이 저장소가 Public 이라 주소를 아는 사람은 앱과 `codes.json`(보유 종목코드), 그 종목들의 종가를 볼 수 있어요. 수량·매수가는 어디에도 올라가지 않아요.
- 자동 갱신이 안 되면 앱에 "종가 기준일이 5일 넘게 지났어요"가 떠요. Actions 탭에서 실패 로그를 확인하세요.
- GitHub 는 저장소에 60일 동안 활동이 없으면 예약 실행을 멈출 수 있어요. 멈추면 Actions 탭에서 다시 켜 주세요.
