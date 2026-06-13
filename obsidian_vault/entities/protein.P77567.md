---
entity_id: "protein.P77567"
entity_type: "protein"
name: "nhoA"
source_database: "UniProt"
source_id: "P77567"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250|UniProtKB:Q00267}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nhoA yddI b1463 JW1458"
---

# nhoA

`protein.P77567`

## Static

- Type: `protein`
- Source: `UniProt:P77567`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250|UniProtKB:Q00267}.

## Enriched Summary

FUNCTION: Catalyzes the acetyl-CoA-dependent N-acetylation of aromatic amines, and, probably, the O-acetylation of N-hydroxyarylamines. In vitro, catalyzes the N-acetylation of various arylamines such as aminobenzoic acid, aminophenol, aminotoluene, phenetidine, anisidine, aniline, isoniazid and 2-amino-fluorene (PubMed:10806332, PubMed:23452042). N-hydroxyarylamine O-acetyltransferase activity has not been assayed directly, however, NhoA activity is required for the mutagenicity of nitroaromatic compounds, suggesting that it also has O-acetyltransferase activity (Probable). {ECO:0000269|PubMed:10806332, ECO:0000269|PubMed:23452042, ECO:0000305|PubMed:12222687, ECO:0000305|PubMed:23452042}. Arylamine acetyltransferase (NhoA) catalyzes the acetyl-CoA-dependent N-acetylation of a variety of arylamine substrates. It acts via a ping-pong bi bi mechanism . The physiological role of NhoA is unknown. Two acetylated lysine residues within NhoA can be deacetylated by G6577-MONOMER "CobB". Mutants of NhoA in which one or both lysine residues have been mutated have lower N-acetyltransferase activity than wild-type . NhoA may also act as an N-hydroxyarylamine O-acetyltransferase, although this activity has not been assayed directly. However, this activity leads to metabolic activation and increased toxicity of nitro compounds...

## Biological Role

Component of arylamine N-acetyltransferase (complex.ecocyc.CPLX0-236).

## Annotation

FUNCTION: Catalyzes the acetyl-CoA-dependent N-acetylation of aromatic amines, and, probably, the O-acetylation of N-hydroxyarylamines. In vitro, catalyzes the N-acetylation of various arylamines such as aminobenzoic acid, aminophenol, aminotoluene, phenetidine, anisidine, aniline, isoniazid and 2-amino-fluorene (PubMed:10806332, PubMed:23452042). N-hydroxyarylamine O-acetyltransferase activity has not been assayed directly, however, NhoA activity is required for the mutagenicity of nitroaromatic compounds, suggesting that it also has O-acetyltransferase activity (Probable). {ECO:0000269|PubMed:10806332, ECO:0000269|PubMed:23452042, ECO:0000305|PubMed:12222687, ECO:0000305|PubMed:23452042}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-236|complex.ecocyc.CPLX0-236]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1463|gene.b1463]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77567`
- `KEGG:ecj:JW1458;eco:b1463;ecoc:C3026_08495;`
- `GeneID:947251;`
- `GO:GO:0004060; GO:0005737; GO:0042803; GO:0046990`
- `EC:2.3.1.118; 2.3.1.5`

## Notes

Arylamine N-acetyltransferase (EC 2.3.1.5) (Arylhydroxamate N,O-acetyltransferase) (N-hydroxyarylamine O-acetyltransferase) (EC 2.3.1.118)
