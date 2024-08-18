# Portfolio Website Generator

1. Clone the Project
```shell
git clone https://github.com/caxefaizan/portfolio_website.git
cd portfolio_website
```
2. Create a virtual environment
```shell
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```
3. Create your profile data as `profiledata.json` in the following format
```json
{
  "basic": {
    "name": "John DOe",
    "email": "john@example.com",
    "contact": "+1234567890",
    "social": "linkedin.com/in/dummy",
    "address": "XX, yy, ZZ"
  },
  "skillset": {
    "frameworks": [
      "Abc"
    ],
    "languages": [
      "Python"
    ],
    "cloud": [
      "GCP"
    ]
  },
  "experiences": [
    {
      "companyName": "XyZ",
      "url": "https://www.xyz.com/",
      "positions": [
        {
          "title": "abc",
          "tenure": {
            "from": "mm/yy",
            "to": "mm/yy"
          }
        }
      ],
      "description": [
        "lorLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
      ]
    }
  ],
  "educations": [
    {
      "title": "Ace of Everything Jack of None",
      "url": "https://www.example.net/",
      "grade": "",
      "tenure": {
        "from": "mm/yy",
        "to": "mm/yy"
      },
      "institute": "example"
    }
  ],
  "certifications": [
    {
      "title": "Certified Developer",
      "url": "https://www.credly.com/badges/xxxx"
    }
  ],
  "softskills": [
    {
      "title": "Example",
      "companyName": "Example",
      "url": "https://www.example.com/",
      "tenure": {
        "from": "mm/yy",
        "to": "mm/yy"
      },
      "description": [
        "lorLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
      ]
    }
  ],
  "externallinks": [
    {
      "title": "lorLorem ipsum dolor sit amet.",
      "url": "https://www.example.com/",
      "imgsource": "./static/assets/images/blogs/udemycourse.jpeg"
    }
  ],
  "socialLinks": [
    {
      "title": "linkedin",
      "url": "https://www.linkedin.com/in/example"
    },
    {
      "title": "medium",
      "url": "https://medium.com/@example"
    },
    {
      "title": "github",
      "url": "https://github.com/example"
    },
    {
      "title": "stack-overflow",
      "url": "https://stackoverflow.com/users/123/example"
    },
    {
      "title": "instagram",
      "url": "http://www.instagram.com/example"
    }
  ]
}
```
4. Run the server
```shell
flask --app webserver run --debug
```