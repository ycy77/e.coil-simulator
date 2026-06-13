---
entity_id: "protein.P32717"
entity_type: "protein"
name: "yjcS"
source_database: "UniProt"
source_id: "P32717"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:25066955}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yjcS b4083 JW5721"
---

# yjcS

`protein.P32717`

## Static

- Type: `protein`
- Source: `UniProt:P32717`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:25066955}.

## Enriched Summary

FUNCTION: Alkylsulfatase that cleaves the widely used detergent sodium dodecyl sulfate (SDS). {ECO:0000269|PubMed:25066955}. Overexpression of yjcS from a plasmid supports growth of E. coli on minimal medium agarose containing 0.1% sodium dodecyl sulfate (SDS). Purified YjcS has sodium dodecyl sulfatase activity in vitro. YjcS contains a conserved HXHXDH catalytic motif that is shared by the experimentally characterised alkyl sulfatases, SdsA1 from Pseudomonas aeruginosa and Pisa1 from Pseudomonas sp. Mutation of two residues in this catalytic motif (D184N H185A) results in loss of sulfatase activity . Crystallised YjcS is homodimeric; each monomer contains an N-terminal domain, a central dimerization domain and a C-terminal domain. The N and C-terminal domains are spatially adjacent and form a hydrophobic channel that leads to a putative active site . YjcS contains an N-terminal signal sequence and is secreted into the periplasm . The promoter of yjcS is predicted to be σ28-dependent and can be transcribed by CPLX0-222 in vitro .

## Biological Role

Catalyzes RXN-15761 (reaction.ecocyc.RXN-15761).

## Annotation

FUNCTION: Alkylsulfatase that cleaves the widely used detergent sodium dodecyl sulfate (SDS). {ECO:0000269|PubMed:25066955}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-15761|reaction.ecocyc.RXN-15761]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4083|gene.b4083]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32717`
- `KEGG:ecj:JW5721;eco:b4083;ecoc:C3026_22075;`
- `GeneID:948597;`
- `GO:GO:0018741; GO:0018909; GO:0030288; GO:0046872; GO:0046983`
- `EC:3.1.6.21`

## Notes

Linear primary-alkylsulfatase (EC 3.1.6.21) (Type III linear primary-alkylsulfatase)
