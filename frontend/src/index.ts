import { client, DefaultService,  } from "./client";

client.setConfig({
  baseURL: 'http://127.0.0.1:8000',
});

async function remoteCall(){
    const response = await DefaultService.readUserByEmailApiV1UsersEmailUserEmailGet({
      query: {
        email: "",
      },
    })
    const data = response.data
    console.log(typeof data)
    console.log(data)
}

remoteCall()