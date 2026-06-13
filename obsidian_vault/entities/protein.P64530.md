---
entity_id: "protein.P64530"
entity_type: "protein"
name: "rcnR"
source_database: "UniProt"
source_id: "P64530"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rcnR yohL b2105 JW2092"
---

# rcnR

`protein.P64530`

## Static

- Type: `protein`
- Source: `UniProt:P64530`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Repressor of rcnA expression. Acts by binding specifically to the rcnA promoter in the absence of nickel and cobalt. In the presence of one of these metals, it has a weaker affinity for rcnA promoter. {ECO:0000269|PubMed:16956381, ECO:0000269|PubMed:17120142}. The RcnR, resistance to cobalt and nickel regulator protein is an addition to the set of transcriptional metallo-regulator proteins of E. coli (some of the main ones are Fur, CueR, CusR, MntR, Zur, ZntR, and NikR) , that regulate the transcriptional expression of a recently described efflux protein, RcnA , to maintain nickel and cobalt homeostasis . The homeostasis of different metals in the cell is constantly monitored, and adequate pathways are activated or repressed to keep the metals within normal levels. Specifically, when nickel and cobalt exceed the normal levels, cell growth stops . Ni(II) and Co(II) binding results in the transcription of RcnAB in vivo, although it has been shown that RcnR binds a variety of metal ions in vitro . Binding of Co(II) and Ni(II) to RcnR affects its flexibility at the N terminus, and this effect modulates its DNA-binding affinity . The rcnR gene is encoded divergently to the rcnA gene, which encodes an efflux protein that is involved in nickel and cobalt homeostasis ; it removes an excess of ions...

## Biological Role

Component of RcnR-Ni2+ (complex.ecocyc.CPLX0-7618), RcnR-Co2+ (complex.ecocyc.CPLX0-7619).

## Annotation

FUNCTION: Repressor of rcnA expression. Acts by binding specifically to the rcnA promoter in the absence of nickel and cobalt. In the presence of one of these metals, it has a weaker affinity for rcnA promoter. {ECO:0000269|PubMed:16956381, ECO:0000269|PubMed:17120142}.

## Outgoing Edges (5)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7618|complex.ecocyc.CPLX0-7618]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-7619|complex.ecocyc.CPLX0-7619]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b2105|gene.b2105]] `RegulonDB` `S` - regulator=RcnR; target=rcnR; function=-
- `represses` --> [[gene.b2106|gene.b2106]] `RegulonDB` `S` - regulator=RcnR; target=rcnA; function=-
- `represses` --> [[gene.b2107|gene.b2107]] `RegulonDB` `S` - regulator=RcnR; target=rcnB; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b2105|gene.b2105]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P64530`
- `KEGG:ecj:JW2092;eco:b2105;ecoc:C3026_11810;`
- `GeneID:86860280;93775089;947114;`
- `GO:GO:0000976; GO:0001217; GO:0005737; GO:0032993; GO:0045892; GO:0046872`

## Notes

Transcriptional repressor RcnR
