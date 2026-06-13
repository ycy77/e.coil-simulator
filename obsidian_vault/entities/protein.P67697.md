---
entity_id: "protein.P67697"
entity_type: "protein"
name: "hicB"
source_database: "UniProt"
source_id: "P67697"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hicB ydcQ b1438 JW1433"
---

# hicB

`protein.P67697`

## Static

- Type: `protein`
- Source: `UniProt:P67697`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Functions as an mRNA interferase antitoxin; overexpression prevents HicA-mediated cessation of cell growth and inhibition of cell proliferation. {ECO:0000269|PubMed:19060138}. HicB acts as the antitoxin of the HicA-HicB toxin-antitoxin system, and it also regulates the transcription of the operon that encodes the toxin-antitoxin system. HicB recognizes and binds an inverted repeat DNA sequence to regulate transcription, suggesting that HicB binds to DNA as a dimer . An HTH motif has been identified in the C terminus of HicB . Overexpression of HicA induces mRNA cleavage and growth inhibition, but not cell death. Expression of HicB neutralizes the effect of HicA . The loss of HicB downregulates the extracytoplasmic stress response mediated by σE and the production of outer membrane vesicles. It reduces the cellular levels of DegP and Spy and downregulates the Cpx response independently of CpxR . hicB insertion mutants suppress the essential nature of RPOE-MONOMER σE . The mRNA interferase activity of the cognate toxin HicA appears to be responsible for this effect; overexpression of any one of three RNA interferase toxins, HicA, HigB or YafQ, suppresses the essentiality of σE . hicB mutants have no detectable growth defect, but are more sensitive to envelope stress...

## Annotation

FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Functions as an mRNA interferase antitoxin; overexpression prevents HicA-mediated cessation of cell growth and inhibition of cell proliferation. {ECO:0000269|PubMed:19060138}.

## Outgoing Edges (2)

- `represses` --> [[gene.b1438|gene.b1438]] `RegulonDB` `C` - regulator=HicB; target=hicB; function=-
- `represses` --> [[gene.b4532|gene.b4532]] `RegulonDB` `C` - regulator=HicB; target=hicA; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1438|gene.b1438]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P67697`
- `KEGG:ecj:JW1433;eco:b1438;`
- `GeneID:93775583;946001;`
- `GO:GO:0003677; GO:0006355; GO:0006950; GO:0040008; GO:0042802; GO:0110001`

## Notes

Antitoxin HicB
