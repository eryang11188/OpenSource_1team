# �������� ���� ������ �ҷ��ɴϴ�.
import game_manager
from player import Player 

def start_game():
    """
    ������ �����ϱ� ���� �غ� �ϰ�, ���� �Ŵ����� ȣ���մϴ�.
    """
    player_character = Player()
    
    # ������ �÷��̾� ������ ������ game_manager�� ���� ������ ���۽�ŵ�ϴ�.
    game_manager.main_loop(player_character)

if __name__ == "__main__":
    start_game()