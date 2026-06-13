---
entity_id: "protein.P67430"
entity_type: "protein"
name: "nemR"
source_database: "UniProt"
source_id: "P67430"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nemR ydhM b1649 JW5874"
---

# nemR

`protein.P67430`

## Static

- Type: `protein`
- Source: `UniProt:P67430`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in response to both electrophiles and reactive chlorine species (RCS) (PubMed:23506073, PubMed:23536188). Represses the transcription of the nemRA-gloA operon by binding to the NemR box (PubMed:18567656, PubMed:23506073, PubMed:23536188). May sense electrophiles, primarily quinones and glyoxals, as redox signals and regulate the redox state by modulating the expression of nemA and gloA (PubMed:23506073). Also uses the oxidation status of HOCl-sensitive cysteine residues to respond to bleach and related RCS (PubMed:23536188). Involved in response to methylglyoxal (PubMed:23646895). {ECO:0000269|PubMed:18567656, ECO:0000269|PubMed:23506073, ECO:0000269|PubMed:23536188, ECO:0000269|PubMed:23646895}. "N-ethylmaleimide reductase repressor," represses the nemA gene, which is involved in reductive degradation of N-ethylmaleimide (NEM) and other toxic nitrous compounds, and it also represses its own expression. NemR belongs to the TetR family of HTH-type DNA-binding transcription factors . NemR binds to a region 16 bp in length, and its consensus is a palindromic sequence, TAGACCnnnnGGTCTA, which is referred as the NemR box . This box sequence, TAGACCnnnnGGTCTA, is close to the recognition sequence, TTGACCAnnTGGTCAA, of RutR (the RutR box)...

## Biological Role

Component of NemR-methylglyoxal (complex.ecocyc.CPLX0-7716).

## Annotation

FUNCTION: Involved in response to both electrophiles and reactive chlorine species (RCS) (PubMed:23506073, PubMed:23536188). Represses the transcription of the nemRA-gloA operon by binding to the NemR box (PubMed:18567656, PubMed:23506073, PubMed:23536188). May sense electrophiles, primarily quinones and glyoxals, as redox signals and regulate the redox state by modulating the expression of nemA and gloA (PubMed:23506073). Also uses the oxidation status of HOCl-sensitive cysteine residues to respond to bleach and related RCS (PubMed:23536188). Involved in response to methylglyoxal (PubMed:23646895). {ECO:0000269|PubMed:18567656, ECO:0000269|PubMed:23506073, ECO:0000269|PubMed:23536188, ECO:0000269|PubMed:23646895}.

## Outgoing Edges (4)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7716|complex.ecocyc.CPLX0-7716]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b1649|gene.b1649]] `RegulonDB` `S` - regulator=NemR; target=nemR; function=-
- `represses` --> [[gene.b1650|gene.b1650]] `RegulonDB` `S` - regulator=NemR; target=nemA; function=-
- `represses` --> [[gene.b1651|gene.b1651]] `RegulonDB` `S` - regulator=NemR; target=gloA; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1649|gene.b1649]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P67430`
- `KEGG:ecj:JW5874;eco:b1649;ecoc:C3026_09465;`
- `GeneID:75204494;946166;`
- `GO:GO:0003677; GO:0003700; GO:0045892`

## Notes

HTH-type transcriptional repressor NemR (Bleach-sensing transcription factor) (Redox-regulated transcription factor NemR)
