# coding = utf-8

from config import *
def log_path():
    files = os.listdir(PROJECT_DIR + '\\testlog')
    file = PROJECT_DIR + '\\testlog\\' + files[-1]
    return file


def read_log():
    file = log_path()
    with open(file,  'r+', encoding='utf-8') as f:
        log_lines = f.readlines()
        contents = ['test_click_start_lunbo', 'test_choose_virtual_list_item',
                    'test_choose_handup', 'test_choose_pdf_file', 'test_send_chat_text',
                    'test_click_reward_all', 'test_draw', 'test_use_rubber', 'test_choose_virtual_list_item',
                    'test_choose_mp4_file', 'test_choose_ppt_file', 'test_open_video', 'test_start_response',
                    'test_desk_share_open', 'test_tea_share_open', 'test_stu_share_open',
                    'test_use_pdf', 'test_pdf_page_down', 'test_pdf_next_page', 'test_pdf_prev_page',
                    'test_use_mp4', 'test_start_mp4', 'test_mp4_slider', 'test_mp4_loop',
                    'test_use_ppt', 'test_ppt_next_page', 'test_pdf_prev_page',
                    'test_reward_rank_tool', 'test_rank_win_close',
                    'test_start_response', 'test_restart_response', 'test_close_response',
                    'test_answer_setting', 'test_answer_start', 'test_answer_edit', 'test_answer_end',
                    'test_eidt_url', 'test_save_blackboard_ensure',
                    'test_rubber_clear', 'test_quit_classroom', 'test_quit_app']
        for j in range(len(contents)):
            for i in range(len(log_lines)):
                if contents[j] in log_lines[i]:
                    print(log_lines[i])


read_log()
