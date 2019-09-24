# Vue와 Firebase로 모던웹사이트 만들기 강좌 002

##### 1. vue create test

- Manually select feature
  - Babel
  - Router
  - Vuex
  - Linter / Formatter
  - history mode -> yes
  - esLint - standard config
  - In dedicated config files
  - No save

 - 필수 Extension
    - vetur
    - vuetify 설치
        - vue add vuetify
        - Configure(advanced), Material Dsign Icons 말고 전부 enter
    - task Explorer
    - vuetify-vscode : 스니펫(코드 조각)을 잘 만들어줌
    - eslint : 규약에 맞게 알아서 이쁘게 만들어줌
        - files.autoSave : onFocusChange
        
        - ```json
          "eslint.validate": [
                  {"language":"javascript","autoFix": true},
                  {"language":"vue","autoFix": true},
                  {"language":"html","autoFix": true},
              ]
          ```
        
    - mdi(Material Dsign Icons) : Icon keyword 알려줌