---
entity_id: "protein.P76256"
entity_type: "protein"
name: "tsaB"
source_database: "UniProt"
source_id: "P76256"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:19376873}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tsaB yeaZ b1807 JW1796"
---

# tsaB

`protein.P76256`

## Static

- Type: `protein`
- Source: `UniProt:P76256`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:19376873}.

## Enriched Summary

FUNCTION: Required for the formation of a threonylcarbamoyl group on adenosine at position 37 (t(6)A37) in tRNAs that read codons beginning with adenine. Is probably involved in the transfer of the threonylcarbamoyl moiety of threonylcarbamoyl-AMP (TC-AMP) to the N6 group of A37, together with TsaD and TsaE. TsaB seems to play an indirect role in the t(6)A biosynthesis pathway, possibly in regulating the core enzymatic function of TsaD. In fact, can act as a protease that specifically degrades TsaD in vitro; therefore TsaB may post-translationally regulate cellular pools of TsaD via proteolytic degradation. Does not show sialoglycoprotease activity against glycophorin A. {ECO:0000269|PubMed:19376873, ECO:0000269|PubMed:22378793}. TsaB is involved in the biosynthesis of the threonylcarbamoyladenosine (t6A) residue at position 37 of ANN-decoding tRNAs. A mixture of purified G7698-MONOMER TsaC, EG11171-MONOMER TsaD, TsaB, and EG11757-MONOMER TsaE proteins catalyzes formation of t6A in the presence of a tRNA substrate, ATP, threonine and bicarbonate in vitro . The three essential proteins TsaE, TsaB and TsaD form an interaction network. TsaB interacts with itself; it can interact with both TsaE and TsaD directly, and the interactions appear to be mutually exclusive . The specific interaction between TsaD and TsaB is required for the essential function of these proteins...

## Biological Role

Catalyzes RXN0-5522 (reaction.ecocyc.RXN0-5522). Component of N6-L-threonylcarbamoyladenine synthase, TsaB-TsaD dimer subunit (complex.ecocyc.CPLX0-8181), N6-L-threonylcarbamoyladenine synthase (complex.ecocyc.CPLX0-8182). Bound by Zinc cation (molecule.C00038).

## Annotation

FUNCTION: Required for the formation of a threonylcarbamoyl group on adenosine at position 37 (t(6)A37) in tRNAs that read codons beginning with adenine. Is probably involved in the transfer of the threonylcarbamoyl moiety of threonylcarbamoyl-AMP (TC-AMP) to the N6 group of A37, together with TsaD and TsaE. TsaB seems to play an indirect role in the t(6)A biosynthesis pathway, possibly in regulating the core enzymatic function of TsaD. In fact, can act as a protease that specifically degrades TsaD in vitro; therefore TsaB may post-translationally regulate cellular pools of TsaD via proteolytic degradation. Does not show sialoglycoprotease activity against glycophorin A. {ECO:0000269|PubMed:19376873, ECO:0000269|PubMed:22378793}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5522|reaction.ecocyc.RXN0-5522]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-8181|complex.ecocyc.CPLX0-8181]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-8182|complex.ecocyc.CPLX0-8182]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1807|gene.b1807]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76256`
- `KEGG:ecj:JW1796;eco:b1807;ecoc:C3026_10295;`
- `GeneID:946304;`
- `GO:GO:0000408; GO:0002949; GO:0005829; GO:0008237; GO:0042802; GO:1990145`

## Notes

tRNA threonylcarbamoyladenosine biosynthesis protein TsaB (t(6)A37 threonylcarbamoyladenosine biosynthesis protein TsaB)
