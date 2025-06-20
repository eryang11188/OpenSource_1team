# ������ �ٸ� �������� ���� ���ϵ��� �ҷ��ɴϴ�.
import dungeon  # D������ ���� dungeon.py
import shop     # B������ ���� shop.py

def main_loop(player):
    """
    �÷��̾ ����ִ� ���� ������ ���� ������ ��� �����մϴ�.
    """
    print("\n" + "=" * 30)
    print("�α׶���ũ TRPG�� ���� ���� ȯ���մϴ�!")
    print("=" * 30)

    while player.is_alive(): # B������ ���� player ��ü�� is_alive() �޼��带 ����մϴ�.
        # ���� �÷��̾� ���¸� �����ݴϴ�.
        player.show_status()

        # ����ڿ��� �ൿ�� �����϶�� ��û�մϴ�.
        print("1. ����ͷ� ����")
        print("2. ���� �湮�ϱ�")
        print("3. ���� ����")
        
        choice = input(">> �ൿ �Է� ")

        if choice == '1':
            dungeon.enter_dungeon(player) # D������ ���
        elif choice == '2':
            shop.open_shop(player)        # B������ ���
        elif choice == '3':
            print("������ �����մϴ�.")
            break # while ������ Ż���Ͽ� ������ �����ϴ�.
        else:
            print("�߸��� �Է��Դϴ�.")
        
    print("\nGAME OVER")