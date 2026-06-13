---
entity_id: "protein.P0A8F8"
entity_type: "protein"
name: "uvrB"
source_database: "UniProt"
source_id: "P0A8F8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uvrB b0779 JW0762"
---

# uvrB

`protein.P0A8F8`

## Static

- Type: `protein`
- Source: `UniProt:P0A8F8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: The UvrABC repair system catalyzes the recognition and processing of DNA lesions. A damage recognition complex composed of 2 UvrA and 2 UvrB subunits scans DNA for abnormalities. Upon binding of the UvrA(2)B(2) complex to a putative damaged site, the DNA wraps around one UvrB monomer. DNA wrap is dependent on ATP binding by UvrB and probably causes local melting of the DNA helix, facilitating insertion of UvrB beta-hairpin between the DNA strands. Then UvrB probes one DNA strand for the presence of a lesion. If a lesion is found the UvrA subunits dissociate and the UvrB-DNA preincision complex is formed. This complex is subsequently bound by UvrC and the second UvrB is released. If no lesion is found, the DNA wraps around the other UvrB subunit that will check the other stand for damage. {ECO:0000269|PubMed:12145219}. Deletion of uvrB results in a significant decrease in persister fraction following fluoroquinolone treatment; the absence of uvrB impedes persister awakening .

## Biological Role

Component of excision nuclease UvrABC (complex.ecocyc.UVRABC-CPLX).

## Enriched Pathways

- `eco03420` Nucleotide excision repair (KEGG)

## Annotation

FUNCTION: The UvrABC repair system catalyzes the recognition and processing of DNA lesions. A damage recognition complex composed of 2 UvrA and 2 UvrB subunits scans DNA for abnormalities. Upon binding of the UvrA(2)B(2) complex to a putative damaged site, the DNA wraps around one UvrB monomer. DNA wrap is dependent on ATP binding by UvrB and probably causes local melting of the DNA helix, facilitating insertion of UvrB beta-hairpin between the DNA strands. Then UvrB probes one DNA strand for the presence of a lesion. If a lesion is found the UvrA subunits dissociate and the UvrB-DNA preincision complex is formed. This complex is subsequently bound by UvrC and the second UvrB is released. If no lesion is found, the DNA wraps around the other UvrB subunit that will check the other stand for damage. {ECO:0000269|PubMed:12145219}.

## Pathways

- `eco03420` Nucleotide excision repair (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.UVRABC-CPLX|complex.ecocyc.UVRABC-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0779|gene.b0779]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8F8`
- `KEGG:ecj:JW0762;eco:b0779;ecoc:C3026_04945;`
- `GeneID:93776651;945385;`
- `GO:GO:0000715; GO:0003677; GO:0005524; GO:0005737; GO:0006289; GO:0006294; GO:0009314; GO:0009380; GO:0009381; GO:0009432; GO:0016887; GO:0042802`

## Notes

UvrABC system protein B (Protein UvrB) (Excinuclease ABC subunit B)
