---
entity_id: "protein.P0AF67"
entity_type: "protein"
name: "tsaE"
source_database: "UniProt"
source_id: "P0AF67"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:19376873}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tsaE yjeE b4168 JW4126"
---

# tsaE

`protein.P0AF67`

## Static

- Type: `protein`
- Source: `UniProt:P0AF67`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:19376873}.

## Enriched Summary

FUNCTION: Required for the formation of a threonylcarbamoyl group on adenosine at position 37 (t(6)A37) in tRNAs that read codons beginning with adenine. Is probably involved in the transfer of the threonylcarbamoyl moiety of threonylcarbamoyl-AMP (TC-AMP) to the N6 group of A37, together with TsaD and TsaB. TsaE seems to play an indirect role in the t(6)A biosynthesis pathway, possibly in regulating the core enzymatic function of TsaD. Displays ATPase activity in vitro. {ECO:0000269|PubMed:22378793}. TsaE is involved in the biosynthesis of the threonylcarbamoyladenosine (t6A) residue at position 37 of ANN-decoding tRNAs. A mixture of purified G7698-MONOMER TsaC, EG11171-MONOMER TsaD, G6991-MONOMER TsaB, and TsaE proteins catalyzes formation of t6A in the presence of a tRNA substrate, ATP, threonine and bicarbonate in vitro . The three essential proteins TsaE, TsaB and TsaD form an interaction network. TsaB can interact with both TsaE and TsaD directly, and the interactions appear to be mutually exclusive . Purified TsaE forms a heterogeneous mixture of oligomers in vitro . The protein is broadly conserved in bacteria and contains motifs characteristic of P-loop ATPases . A crystal structure of Haemophilus influenzae TsaE shows a nucleotide binding fold . Measurements of TsaE's low intrinsic ATPase activity and ADP binding vary; measured ATPase activity with a Km of 1...

## Biological Role

Component of N6-L-threonylcarbamoyladenine synthase (complex.ecocyc.CPLX0-8182).

## Annotation

FUNCTION: Required for the formation of a threonylcarbamoyl group on adenosine at position 37 (t(6)A37) in tRNAs that read codons beginning with adenine. Is probably involved in the transfer of the threonylcarbamoyl moiety of threonylcarbamoyl-AMP (TC-AMP) to the N6 group of A37, together with TsaD and TsaB. TsaE seems to play an indirect role in the t(6)A biosynthesis pathway, possibly in regulating the core enzymatic function of TsaD. Displays ATPase activity in vitro. {ECO:0000269|PubMed:22378793}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8182|complex.ecocyc.CPLX0-8182]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4168|gene.b4168]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AF67`
- `KEGG:ecj:JW4126;eco:b4168;ecoc:C3026_22525;`
- `GeneID:86861438;93777653;948684;`
- `GO:GO:0000408; GO:0002949; GO:0004672; GO:0005524; GO:0005737; GO:0016887; GO:0042802; GO:0043531; GO:0046872; GO:1990145`

## Notes

tRNA threonylcarbamoyladenosine biosynthesis protein TsaE (t(6)A37 threonylcarbamoyladenosine biosynthesis protein TsaE)
