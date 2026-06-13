---
entity_id: "protein.P25524"
entity_type: "protein"
name: "codA"
source_database: "UniProt"
source_id: "P25524"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "codA b0337 JW0328"
---

# codA

`protein.P25524`

## Static

- Type: `protein`
- Source: `UniProt:P25524`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolytic deamination of cytosine to uracil. Is involved in the pyrimidine salvage pathway, which allows the cell to utilize cytosine for pyrimidine nucleotide synthesis. Is also able to catalyze deamination of isoguanine, a mutagenic oxidation product of adenine in DNA, and of isocytosine. To a lesser extent, also catalyzes the conversion of 5-fluorocytosine (5FC) to 5-fluorouracil (5FU); this activity allows the formation of a cytotoxic chemotherapeutic agent from a non-cytotoxic precursor. {ECO:0000269|PubMed:15381761, ECO:0000269|PubMed:21545144, ECO:0000269|PubMed:21604715, ECO:0000269|PubMed:8226944}.

## Biological Role

Component of cytosine/isoguanine deaminase (complex.ecocyc.CPLX0-7932).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolytic deamination of cytosine to uracil. Is involved in the pyrimidine salvage pathway, which allows the cell to utilize cytosine for pyrimidine nucleotide synthesis. Is also able to catalyze deamination of isoguanine, a mutagenic oxidation product of adenine in DNA, and of isocytosine. To a lesser extent, also catalyzes the conversion of 5-fluorocytosine (5FC) to 5-fluorouracil (5FU); this activity allows the formation of a cytotoxic chemotherapeutic agent from a non-cytotoxic precursor. {ECO:0000269|PubMed:15381761, ECO:0000269|PubMed:21545144, ECO:0000269|PubMed:21604715, ECO:0000269|PubMed:8226944}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7932|complex.ecocyc.CPLX0-7932]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b0337|gene.b0337]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25524`
- `KEGG:ecj:JW0328;eco:b0337;ecoc:C3026_01650;ecoc:C3026_24820;`
- `GeneID:944996;`
- `GO:GO:0004131; GO:0005829; GO:0006209; GO:0008198; GO:0008270; GO:0035888; GO:0042802`
- `EC:3.5.4.-; 3.5.4.1`

## Notes

Cytosine deaminase (CD) (CDA) (CDase) (EC 3.5.4.1) (Cytosine aminohydrolase) (Isoguanine deaminase) (EC 3.5.4.-)
