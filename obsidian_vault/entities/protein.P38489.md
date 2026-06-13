---
entity_id: "protein.P38489"
entity_type: "protein"
name: "nfsB"
source_database: "UniProt"
source_id: "P38489"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nfsB dprA nfnB nfsI ntr b0578 JW0567"
---

# nfsB

`protein.P38489`

## Static

- Type: `protein`
- Source: `UniProt:P38489`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Reduction of a variety of nitroaromatic compounds using NADH (and to lesser extent NADPH) as source of reducing equivalents; two electrons are transferred. Capable of reducing nitrofurazone, quinones and the anti-tumor agent CB1954 (5-(aziridin-1-yl)-2,4-dinitrobenzamide). The reduction of CB1954 results in the generation of cytotoxic species. {ECO:0000269|PubMed:15684426}. The nfsB-encoded nitroreductase is the minor oxygen-insensitive nitroreductase present in E. coli K-12. NfsB reduces a broad range of nitroaromatic compounds , including the antibiotics nitrofurazone and nitrofurantoin . NfsB is a flavin mononucleotide (FMN)-containing protein and uses both NADH and NADPH as a source of reducing equivalents . FAD can substitute for FMN as an effective prosthetic group . NfsB catalyzes the reduction of nitrocompounds using a ping-pong Bi-Bi mechanism . The reduction of nitroaromatic compounds consists of two successive, two-electron transfer reactions to reduce nitroaromatics to their hydroxylamine derivatives . NfsB can also act as a ferric reductase and catalyze a one-electron reduction of hydrogen peroxide, forming hydroxyl radicals . In the presence of free flavins, NfsB is able to release ferrous iron from FtnA and Bfr; NfsB also has a free flavin reductase activity with NADH as the electron donor...

## Biological Role

Component of NAD(P)H-dependent nitroreductase NfsB (complex.ecocyc.DIHYDROPTERIREDUCT-CPLX).

## Enriched Pathways

- `eco00633` Nitrotoluene degradation (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Reduction of a variety of nitroaromatic compounds using NADH (and to lesser extent NADPH) as source of reducing equivalents; two electrons are transferred. Capable of reducing nitrofurazone, quinones and the anti-tumor agent CB1954 (5-(aziridin-1-yl)-2,4-dinitrobenzamide). The reduction of CB1954 results in the generation of cytotoxic species. {ECO:0000269|PubMed:15684426}.

## Pathways

- `eco00633` Nitrotoluene degradation (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.DIHYDROPTERIREDUCT-CPLX|complex.ecocyc.DIHYDROPTERIREDUCT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0578|gene.b0578]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P38489`
- `KEGG:ecj:JW0567;eco:b0578;ecoc:C3026_02870;`
- `GeneID:945778;`
- `GO:GO:0003955; GO:0004155; GO:0005829; GO:0010181; GO:0016020; GO:0016491; GO:0042802; GO:0042803; GO:0046256`
- `EC:1.-.-.-; 1.5.1.34`

## Notes

Oxygen-insensitive NAD(P)H nitroreductase (EC 1.-.-.-) (Dihydropteridine reductase) (EC 1.5.1.34) (FMN-dependent nitroreductase)
