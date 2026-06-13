---
entity_id: "protein.P77791"
entity_type: "protein"
name: "maa"
source_database: "UniProt"
source_id: "P77791"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "maa ylaD b0459 JW0448"
---

# maa

`protein.P77791`

## Static

- Type: `protein`
- Source: `UniProt:P77791`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the CoA-dependent transfer of an acetyl group to maltose and other sugars (PubMed:1856235). Acetylates glucose exclusively at the C6 position and maltose at the C6 position of the non-reducing end glucosyl moiety. Is able to acetylate maltooligosaccharides (PubMed:12731863). {ECO:0000269|PubMed:12731863, ECO:0000269|PubMed:1856235}. Maltose O-acetyltransferase has broad substrate specificity, and is capable of acetylating many sugars. The enzyme is not part of the maltose system. Its specific physiological role is not known, but it is thought that the enzyme prevents the accumulation of free sugars to high levels through acetylation, playing a detoxifying role in the cell . Acetylmaltose is excreted into the culture medium in malB+ malQ strains, which accumulate maltose, but cannot metabolize it . The enzyme belongs to the hexapeptide repeat family of proteins. A crystal structure has been solved at 2.15 Å resolution . The most effective substrate is glucose, which is acetylated at the C6 position; maltose is acetylated at C6 of the nonreducing glucose moiety . Mac: "maltose transacetylase"

## Biological Role

Component of maltose O-acetyltransferase (complex.ecocyc.MALTACETYLTRAN-CPLX).

## Annotation

FUNCTION: Catalyzes the CoA-dependent transfer of an acetyl group to maltose and other sugars (PubMed:1856235). Acetylates glucose exclusively at the C6 position and maltose at the C6 position of the non-reducing end glucosyl moiety. Is able to acetylate maltooligosaccharides (PubMed:12731863). {ECO:0000269|PubMed:12731863, ECO:0000269|PubMed:1856235}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.MALTACETYLTRAN-CPLX|complex.ecocyc.MALTACETYLTRAN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b0459|gene.b0459]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77791`
- `KEGG:ecj:JW0448;eco:b0459;ecoc:C3026_02250;`
- `GeneID:93776991;945096;`
- `GO:GO:0008374; GO:0008925; GO:0032991; GO:0042802`
- `EC:2.3.1.79`

## Notes

Maltose O-acetyltransferase (MAT) (EC 2.3.1.79) (Maltose transacetylase)
