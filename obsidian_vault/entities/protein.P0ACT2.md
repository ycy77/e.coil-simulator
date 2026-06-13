---
entity_id: "protein.P0ACT2"
entity_type: "protein"
name: "envR"
source_database: "UniProt"
source_id: "P0ACT2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "envR yhdK b3264 JW3232"
---

# envR

`protein.P0ACT2`

## Static

- Type: `protein`
- Source: `UniProt:P0ACT2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Potential regulator protein for the acrEF/envCD genes. EnvR, also known as AcrS, represses the transcription of genes encoding a drug efflux pump that has a role in resistance to antibiotics . This protein is homologous to some other proteins, such as MtrR of Neisseria gonorrhoeae, TcmR of Streptomyces glaucescens, JadR2 from Streptomyces venezuelae, and AcrR from Escherichia coli . All of these proteins, including EnvR, have a helix-turn-helix motif close to the N terminus . EnvR recognizes and binds a 24-bp palindromic DNA sequence . The same sequence is also recognized by the transcriptional repressor AcrR . envR is adjacent and divergent in the genome to acrEF, an operon that encodes another drug efflux pump; however, it is not regulated or is only lightly affected by EnvR . Both of these transcription units appears to be repressed by HNS . Based on wide-scale analyses, the conservation of the TetR-family transcriptional regulators (TFTRs) across two genera, Escherichia and Salmonella, were analyzed and compared on three levels: genus, species, and strain. acrR, envR, and nemR TFTR genes were present in all Gram-negative species (Escherichia, Salmonella, P. aeruginosa, and K. pneumoniae), and these were denoted as core. On the other hand, slmA and ybiH genes were not present in all species but were present in all Escherichia and Salmonella species...

## Annotation

FUNCTION: Potential regulator protein for the acrEF/envCD genes.

## Outgoing Edges (2)

- `represses` --> [[gene.b0462|gene.b0462]] `RegulonDB` `S` - regulator=EnvR; target=acrB; function=-
- `represses` --> [[gene.b0463|gene.b0463]] `RegulonDB` `S` - regulator=EnvR; target=acrA; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3264|gene.b3264]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACT2`
- `KEGG:ecj:JW3232;eco:b3264;ecoc:C3026_17755;`
- `GeneID:75206112;947704;`
- `GO:GO:0003677; GO:0003700; GO:0009410; GO:0032993; GO:0045892`

## Notes

Probable acrEF/envCD operon repressor
