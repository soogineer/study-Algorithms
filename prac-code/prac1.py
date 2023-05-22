def solution(board):
    n = len(board) # 'n'에는 게임화면의 가로 또는 세로길이가 저장됨. 'len(board)를 통해 구함'
    answer = -1 # 변수 answer을 -1로 초기화해줌 => 힌트를 줄 수 있는 경우의 수 저장함

    # 사탕을 서로 바꾸는 함수
    def swap(i, j, ni, nj):
        board[i][j], board[ni][nj] = board[ni][nj], board[i][j] # 주어진 좌표 [i][j]와[ni][nj]에 위치한 사탕의 위치 서로 바꿈

    # 가로 방향으로 연속된 사탕 개수 확인
    def check_row(): 
        for i in range(n): # 이중반복문을 사용해 모든 행과 열에 대해 인접한 세 개의 사탕이 같은지 확인
            for j in range(n - 2):
                if board[i][j] == board[i][j + 1] == board[i][j + 2]: 
                    return True
        return False

    # 세로 방향으로 연속된 사탕 개수 확인
    def check_col(): 
        for i in range(n - 2): # 이중반복문을 사용해 모든 열과 행에 대해 인접한 세 개의 사탕이 같은지 확인
            for j in range(n):
                if board[i][j] == board[i + 1][j] == board[i + 2][j]: #
                    return True
        return False

    # 사탕을 서로 바꿔가며 힌트를 줄 수 있는 경우의 수 계산
    def calculate(): 
        cnt = 0
        for i in range(n):
            for j in range(n):
                if i < n - 1: # 이중 반복문을 사용해 게임화면의 모든 위치 확인
                    swap(i, j, i + 1, j)
                    if check_row() or check_col(): 
                        cnt += 1
                    swap(i, j, i + 1, j) # 만약 현재 위치 [i][j]와 아래쪽 위치[i+1][j]를 바꿨을 때, 가로방향 또는 세로방향에 연속된 사탕이 3개 있다면 'cnt' 값 증가
                if j < n - 1:
                    swap(i, j, i, j + 1) # 만약 현재 위치 [i][j]와 아래쪽 위치[i][j+1]를 바꿨을 때, 가로방향 또는 세로방향에 연속된 사탕이 3개 있다면 'cnt' 값 증가
                    if check_row() or check_col():
                        cnt += 1
                    swap(i, j, i, j + 1)
        return cnt # 모든 경우의 수에 대해 'cnt'값 계산하고 반환

    # 모든 경우를 고려하여 힌트를 줄 수 있는 경우의 수 계산
    answer = calculate() # 'calculate()'함수 호출해 결과 얻고

    if answer == 0: # 결과가 0이면 '-1'로 대체
        answer = -1

    return answer
