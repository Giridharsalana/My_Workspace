use std::collections::HashMap;

async fn req() -> Result<(), Box<dyn std::error::Error>> {
    let resp = reqwest::get("https://httpbin.org/ip")
        .await?
        .json::<HashMap<String, String>>()
        .await?;
    println!("{:#?}", resp);
    Ok(())
}

#[tokio::main]
async fn main() {
    one();
    let one = req().await;
    println!("{:?}", one)
    
}