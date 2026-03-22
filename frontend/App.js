import React, { useState } from 'react';
import { StyleSheet, Text, View, Button, Platform } from 'react-native';

export default function App() {
  const [resposta, setResposta] = useState("Aguardando teste...");

  const testarConexao = async () => {
    try {
      setResposta("Carregando...");

      // Se for web, usa o localhost. Se for mobile, puxa o IP do .env
      const baseUrl = Platform.OS === 'web'
        ? 'http://localhost:8000'
        : process.env.EXPO_PUBLIC_API_URL;

      // Montamos a URL final juntando a base com o endpoint
      const endpoint = `${baseUrl}/api/ping/`;

      console.log(`Testando conexão em: ${endpoint}`); // Ajuda no debug do terminal

      const res = await fetch(endpoint);
      const data = await res.json();
      setResposta(data.message);

    } catch (error) {
      setResposta("Erro de conexão: " + error.message);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.texto}>{resposta}</Text>
      <Button title="Testar Backend" onPress={testarConexao} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  texto: { fontSize: 18, marginBottom: 20, textAlign: 'center', padding: 20 }
});