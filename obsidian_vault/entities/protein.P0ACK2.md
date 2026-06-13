---
entity_id: "protein.P0ACK2"
entity_type: "protein"
name: "agaR"
source_database: "UniProt"
source_id: "P0ACK2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "agaR yhaW b3131 JW3100"
---

# agaR

`protein.P0ACK2`

## Static

- Type: `protein`
- Source: `UniProt:P0ACK2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Probable repressor for the aga operon for N-acetyl galactosamine transport and metabolism. "N-acetylgalactosamine repressor," AgaR, negatively controls the expression of the aga gene cluster, which is involved in transport and catabolism of N-acetylgalactosamine and d-galactosamine . It is negatively autoregulated and coordinately represses transcription of the divergent agaZVWEFA operon, which is related to transport and degradation of N-acetylgalactosamine . This repressor responds to N-acetylgalactosamine and d-galactosamine in the medium. As a member of the DeoR/GlpR family of transcriptional regulators , AgaR features an N-terminal domain containing a helix-turn-helix motif and a C-terminal domain that includes the key residues involved in co-inducer recognition and oligomerization . In accordance with other helix-turn-helix DNA-binding repressors, AgaR may bind to DNA as a tetramer. Although AgaR represses transcription, it appears to be able to stabilize the RNApol but causes a slow rate of promoter escape . AgaR binds in tandem to several repeat sequences in the intergenic regions of agaZp, agaRp, and agaSp to repress transcription by overlapping the -35 and -10 boxes. The binding targets for AgaR consist of 24-nucleotide-long repeat sequences that possess conserved motifs...

## Annotation

FUNCTION: Probable repressor for the aga operon for N-acetyl galactosamine transport and metabolism.

## Outgoing Edges (9)

- `represses` --> [[gene.b3131|gene.b3131]] `RegulonDB` `S` - regulator=AgaR; target=agaR; function=-
- `represses` --> [[gene.b3132|gene.b3132]] `RegulonDB` `S` - regulator=AgaR; target=kbaZ; function=-
- `represses` --> [[gene.b3133|gene.b3133]] `RegulonDB` `S` - regulator=AgaR; target=agaV; function=-
- `represses` --> [[gene.b3136|gene.b3136]] `RegulonDB` `S` - regulator=AgaR; target=agaS; function=-
- `represses` --> [[gene.b3137|gene.b3137]] `RegulonDB` `S` - regulator=AgaR; target=kbaY; function=-
- `represses` --> [[gene.b3138|gene.b3138]] `RegulonDB` `S` - regulator=AgaR; target=agaB; function=-
- `represses` --> [[gene.b3139|gene.b3139]] `RegulonDB` `S` - regulator=AgaR; target=agaC; function=-
- `represses` --> [[gene.b3140|gene.b3140]] `RegulonDB` `S` - regulator=AgaR; target=agaD; function=-
- `represses` --> [[gene.b3141|gene.b3141]] `RegulonDB` `S` - regulator=AgaR; target=agaI; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3131|gene.b3131]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACK2`
- `KEGG:ecj:JW3100;eco:b3131;ecoc:C3026_17065;`
- `GeneID:93778853;947636;`
- `GO:GO:0000987; GO:0003677; GO:0006355; GO:0098531`

## Notes

Putative aga operon transcriptional repressor
