---
entity_id: "protein.P05852"
entity_type: "protein"
name: "tsaD"
source_database: "UniProt"
source_id: "P05852"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01445, ECO:0000269|PubMed:19376873}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tsaD gcp ygjD b3064 JW3036"
---

# tsaD

`protein.P05852`

## Static

- Type: `protein`
- Source: `UniProt:P05852`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01445, ECO:0000269|PubMed:19376873}.

## Enriched Summary

FUNCTION: Required for the formation of a threonylcarbamoyl group on adenosine at position 37 (t(6)A37) in tRNAs that read codons beginning with adenine. Is probably involved in the transfer of the threonylcarbamoyl moiety of threonylcarbamoyl-AMP (TC-AMP) to the N6 group of A37, together with TsaE and TsaB. TsaD likely plays a direct catalytic role in this reaction. May also be involved in the metabolism of glycated proteins, but does not show sialoglycoprotease activity against glycophorin A. {ECO:0000269|PubMed:20824107, ECO:0000269|PubMed:21183954, ECO:0000269|PubMed:22378793}. TsaD is involved in the biosynthesis of the threonylcarbamoyladenosine (t6A) residue at position 37 of ANN-decoding tRNAs. A mixture of purified G7698-MONOMER TsaC, TsaD, G6991-MONOMER TsaB, and EG11757-MONOMER TsaE proteins catalyzes formation of t6A in the presence of a tRNA substrate, ATP, threonine and bicarbonate in vitro . The three essential proteins TsaE, TsaB and TsaD form an interaction network. TsaD interacts with TsaB, but not with TsaE. Purified TsaD can oligomerize, with the major form being a dimer . The specific interaction between TsaD and TsaB is required for the essential function of these proteins . TsaB and TsaD form a heterodimer; crystal structures of this protein complex have been solved. The structure shows ADP bound at the dimer interface...

## Biological Role

Component of N6-L-threonylcarbamoyladenine synthase, TsaB-TsaD dimer subunit (complex.ecocyc.CPLX0-8181), N6-L-threonylcarbamoyladenine synthase (complex.ecocyc.CPLX0-8182).

## Annotation

FUNCTION: Required for the formation of a threonylcarbamoyl group on adenosine at position 37 (t(6)A37) in tRNAs that read codons beginning with adenine. Is probably involved in the transfer of the threonylcarbamoyl moiety of threonylcarbamoyl-AMP (TC-AMP) to the N6 group of A37, together with TsaE and TsaB. TsaD likely plays a direct catalytic role in this reaction. May also be involved in the metabolism of glycated proteins, but does not show sialoglycoprotease activity against glycophorin A. {ECO:0000269|PubMed:20824107, ECO:0000269|PubMed:21183954, ECO:0000269|PubMed:22378793}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8181|complex.ecocyc.CPLX0-8181]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-8182|complex.ecocyc.CPLX0-8182]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3064|gene.b3064]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P05852`
- `KEGG:ecj:JW3036;eco:b3064;ecoc:C3026_16740;`
- `GeneID:75173186;947578;`
- `GO:GO:0000287; GO:0000408; GO:0002949; GO:0005506; GO:0005829; GO:0042802; GO:0061711; GO:0140032; GO:1990145`
- `EC:2.3.1.234`

## Notes

tRNA N6-adenosine threonylcarbamoyltransferase (EC 2.3.1.234) (N6-L-threonylcarbamoyladenine synthase) (t(6)A synthase) (t(6)A37 threonylcarbamoyladenosine biosynthesis protein TsaD) (tRNA threonylcarbamoyladenosine biosynthesis protein TsaD)
