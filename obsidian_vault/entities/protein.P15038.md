---
entity_id: "protein.P15038"
entity_type: "protein"
name: "helD"
source_database: "UniProt"
source_id: "P15038"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "helD b0962 JW0945"
---

# helD

`protein.P15038`

## Static

- Type: `protein`
- Source: `UniProt:P15038`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Helicase IV catalyzes the unwinding of duplex DNA in the 3' to 5' direction with respect to the bound single strand in a reaction that is dependent upon the hydrolysis of (d)ATP. {ECO:0000269|PubMed:2822720}. DNA helicase IV (HelD) is an ATP-dependent 3'->5' DNA helicase belonging to the helicase superfamily I . HelD appears to interact with ssDNA by a distributed mechanism; addition of SSB stimulates the DNA unwinding reaction two-fold . The presence of a protein bound to dsDNA substantially inhibits the helicase activity of HelD . The predicted ATP binding site of HelD was investigated by site-directed mutagenesis. Mutants in the conserved Q201 and Y502 residues lead to loss of ATPase activity; the S224H and S224M mutants showed unaffected ATPase and DNA binding activities, but severely reduced helicase activity . There appears to be functional overlap between RecQ helicase, helicase II, and helicase IV . Analysis of combinations of mutants in genes of the RecF pathway revealed synergistic interactions between helD and recF/recO in recombinational repair . In combination with a uvrD amber allele, helD mutations are co-suppressors for a mutation in recJ, which encodes a single-strand DNA-specific exonuclease involved in homologous recombination...

## Biological Role

Catalyzes RXN-11135 (reaction.ecocyc.RXN-11135). Bound by Magnesium cation (molecule.C00305).

## Annotation

FUNCTION: Helicase IV catalyzes the unwinding of duplex DNA in the 3' to 5' direction with respect to the bound single strand in a reaction that is dependent upon the hydrolysis of (d)ATP. {ECO:0000269|PubMed:2822720}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11135|reaction.ecocyc.RXN-11135]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0962|gene.b0962]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15038`
- `KEGG:ecj:JW0945;eco:b0962;ecoc:C3026_05880;`
- `GeneID:946227;`
- `GO:GO:0000725; GO:0003677; GO:0005524; GO:0005829; GO:0016887; GO:0043138`
- `EC:5.6.2.4`

## Notes

DNA helicase IV (EC 5.6.2.4) (75 kDa helicase) (DNA 3'-5' helicase IV)
