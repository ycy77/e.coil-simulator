---
entity_id: "protein.Q47149"
entity_type: "protein"
name: "yafQ"
source_database: "UniProt"
source_id: "Q47149"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yafQ b0225 JW0215"
---

# yafQ

`protein.Q47149`

## Static

- Type: `protein`
- Source: `UniProt:Q47149`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system (PubMed:17263853). A sequence-specific mRNA endoribonuclease that inhibits translation elongation and induces bacterial stasis (PubMed:19210620). Cleavage occurs between the second and third residue of the Lys codon followed by a G or A (5'AAA(G/A)3'), is reading-frame dependent and occurs within the 5' end of most mRNAs (PubMed:19210620). Ribosome-binding confers the sequence specificity and reading frame-dependence (PubMed:19210620). When overexpressed in liquid media YafQ partially inhibits protein synthesis, with a reduction in growth rate and colony growth rate. This effect is counteracted by coexpression with cognate antitoxin DinJ (PubMed:17263853). YafQ and DinJ together bind their own promoter, and repress its expression (PubMed:24898247). {ECO:0000269|PubMed:17263853, ECO:0000269|PubMed:19210620, ECO:0000269|PubMed:24898247}.; FUNCTION: Cell death governed by the MazE-MazF and DinJ-YafQ TA systems seems to play a role in biofilm formation (PubMed:19707553). {ECO:0000269|PubMed:19707553}. YafQ is the toxin of the YafQ-DinJ toxin-antitoxin system and is a BECR-fold toxin in the RelE/ParE superfamily of type II toxin-antitoxin systems . YafQ interacts with the 50S subunit of the ribosome and cleaves mRNAs, thereby inhibiting translation...

## Biological Role

Catalyzes RXN0-5509 (reaction.ecocyc.RXN0-5509). Component of DinJ-YafQ antitoxin/toxin complex / DNA-binding transcriptional repressor (complex.ecocyc.CPLX0-7787), DinJ-YafQ-phosphate (complex.ecocyc.CPLX0-8580).

## Annotation

FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system (PubMed:17263853). A sequence-specific mRNA endoribonuclease that inhibits translation elongation and induces bacterial stasis (PubMed:19210620). Cleavage occurs between the second and third residue of the Lys codon followed by a G or A (5'AAA(G/A)3'), is reading-frame dependent and occurs within the 5' end of most mRNAs (PubMed:19210620). Ribosome-binding confers the sequence specificity and reading frame-dependence (PubMed:19210620). When overexpressed in liquid media YafQ partially inhibits protein synthesis, with a reduction in growth rate and colony growth rate. This effect is counteracted by coexpression with cognate antitoxin DinJ (PubMed:17263853). YafQ and DinJ together bind their own promoter, and repress its expression (PubMed:24898247). {ECO:0000269|PubMed:17263853, ECO:0000269|PubMed:19210620, ECO:0000269|PubMed:24898247}.; FUNCTION: Cell death governed by the MazE-MazF and DinJ-YafQ TA systems seems to play a role in biofilm formation (PubMed:19707553). {ECO:0000269|PubMed:19707553}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5509|reaction.ecocyc.RXN0-5509]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-7787|complex.ecocyc.CPLX0-7787]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8580|complex.ecocyc.CPLX0-8580]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0225|gene.b0225]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q47149`
- `KEGG:ecj:JW0215;eco:b0225;ecoc:C3026_01065;ecoc:C3026_23805;`
- `GeneID:944911;`
- `GO:GO:0003677; GO:0003723; GO:0004521; GO:0006402; GO:0006415; GO:0016892; GO:0040008; GO:0043022; GO:0044010; GO:0045892; GO:0046677; GO:0110001`
- `EC:3.1.-.-`

## Notes

mRNA interferase toxin YafQ (EC 3.1.-.-) (Endoribonuclease YafQ) (Toxin YafQ)
