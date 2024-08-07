import gradio as gr
import numpy as np
from openai import OpenAI
client = OpenAI(api_key="")
model = "gpt-4o"
from readpdf import read_files_to_text

def application_criteria(application):
  completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {"role": "system", "content": "You are ChatGPT, an tool in a company that can help us to review appliant's profile. You only speak traditional chinese"},
      {"role": "user", "content": "Now i will provide you applicant's profile and you would analyze the whole profile and give us their score of their ability in different aspects from 1 to 5. The aspects would be 工作穩定性：符合以下兩者條件之一為不穩定，近期兩份工作不滿一，者為不穩定，近期三份工作皆為0~2年為不穩定   技術符合度(有涵蓋越多條件越加分，分數有權重差別)：技術判斷條件：後端>前端>資料庫>輔助技術 後端：Java/C#/.Net  框架：Java - Spring Boot > Spring MVC > JSP / Servlet .Net - .Net7 > .Net6 >.Net Core > .Net MVC > .Net Webform > .Net Winform > VB.Net    資料庫：MySQL/SQL Server/MSSQL/Oracle 資料庫互動：Mybatis / Spring Data JPA / Hibernate / Entity Framework  期待薪資預測：薪資預測公式 = 42500 + 軟體開發相關工作年資(很重要 先確定是否為相關工作) (年) * 4000，正負5000為正常區間。有期待薪資則比較薪資期待是否在正常區間無期待薪資或面議時，根據履歷資料進行判斷：若有股份有限公司經歷則會需要特別增加風險層級，1家股份有限公司 = 薪資期待中機率偏高 2家以上 = 薪資期待高機率偏高符合特定產業類別需要增加風險層級：物流業、放貸產業、計程車業、房屋仲介業者 符合特定高薪名單需要增加風險層級：(待整理) 外商、叡揚、環鴻科技、鈦坦  自傳中是否有提到自己未來希望期待的工作或直接擷取履歷中的兩處期待職缺評估一致性或是否符合期待職缺 make sure the score only comes from their profile.  give us his/her personal information at the beginning. give us the reason of your rating below the score"},
      {"role": "user", "content": application},
    ],
    temperature=0.0
  )
  return completion.choices[0].message.content
def process_multi_file(txt, slid, multiple_files):
    texts = read_files_to_text(multiple_files)
    return "\n\n".join(application_criteria(texts))



demo = gr.Interface(
    fn=process_multi_file,
    inputs=["text","slider", gr.UploadButton("Upload a file", file_count="multiple")],
    outputs=["text"],
)

if __name__ == "__main__":
    demo.launch()