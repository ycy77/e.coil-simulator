---
entity_id: "complex.ecocyc.CPLX0-301"
entity_type: "complex"
name: "3-octaprenyl-4-hydroxybenzoate decarboxylase"
source_database: "EcoCyc"
source_id: "CPLX0-301"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 3-octaprenyl-4-hydroxybenzoate decarboxylase

`complex.ecocyc.CPLX0-301`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-301`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AAB4|protein.P0AAB4]]

## Enriched Summary

3-Octaprenyl-4-hydroxybenzoate decarboxylase (UbiD) is an enzyme of the PWY-6708 pathway that catalyzes the decarboxylation of 3-octaprenyl-4-hydroxybenzoate. It has long been known that UbiD requires a membrane fraction (or phospholipids) and an initially unidentified soluble cofactor for optimal activity . A second protein, UBIX-MONOMER UbiX, was initially proposed to be an isozyme of UbiD , although the proteins do not show amino acid sequence similarity , and no biochemical data for the activity of UbiX existed at that time. Based on genetic interactions between ubiX and ubiD as well as their mutant phenotypes, it was proposed that UbiX and UbiD interact to be able to carry out the 3-octaprenyl-4-hydroxybenzoate decarboxylase step in ubiquinone biosynthesis during logarithmic growth . UbiD is found in both the cytosolic and membrane fractions. UbiD and UbiX co-migrate and may form a 700 kDa complex in the cytosol . Recent data obtained for fungal homologs of UbiD and UbiX have suggested that UbiX synthesizes a CPD-18260 cofactor that is essential for UbiD activity ( and commented in ; see the summary for UBIX-MONOMER UbiX). However, efforts to assay the activity of purified and prFMN-reconstituted E. coli UbiD have so far failed, and oxidative maturation of prFMN within UbiD stalls at the formation of a radical prFMN species...

## Biological Role

Catalyzes 3-OCTAPRENYL-4-OHBENZOATE-DECARBOX-RXN (reaction.ecocyc.3-OCTAPRENYL-4-OHBENZOATE-DECARBOX-RXN). Bound by Prenylated FMNH2 (molecule.C21215), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

3-Octaprenyl-4-hydroxybenzoate decarboxylase (UbiD) is an enzyme of the PWY-6708 pathway that catalyzes the decarboxylation of 3-octaprenyl-4-hydroxybenzoate. It has long been known that UbiD requires a membrane fraction (or phospholipids) and an initially unidentified soluble cofactor for optimal activity . A second protein, UBIX-MONOMER UbiX, was initially proposed to be an isozyme of UbiD , although the proteins do not show amino acid sequence similarity , and no biochemical data for the activity of UbiX existed at that time. Based on genetic interactions between ubiX and ubiD as well as their mutant phenotypes, it was proposed that UbiX and UbiD interact to be able to carry out the 3-octaprenyl-4-hydroxybenzoate decarboxylase step in ubiquinone biosynthesis during logarithmic growth . UbiD is found in both the cytosolic and membrane fractions. UbiD and UbiX co-migrate and may form a 700 kDa complex in the cytosol . Recent data obtained for fungal homologs of UbiD and UbiX have suggested that UbiX synthesizes a CPD-18260 cofactor that is essential for UbiD activity ( and commented in ; see the summary for UBIX-MONOMER UbiX). However, efforts to assay the activity of purified and prFMN-reconstituted E. coli UbiD have so far failed, and oxidative maturation of prFMN within UbiD stalls at the formation of a radical prFMN species . Crystal structures of UbiD in complex with prFMN have been solved, showing the quarternary structure as a trimer-of-dimers homohexamer . The crystal structures show no obvious surface features that would suggest membrane association and no hydrophobic binding site for the octaprenyl tail of the presumed substrate. It is thus possible that the prenyltransfer step currently thought to occur early in the pathway in fact occurs after ring modifica

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3-OCTAPRENYL-4-OHBENZOATE-DECARBOX-RXN|reaction.ecocyc.3-OCTAPRENYL-4-OHBENZOATE-DECARBOX-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C21215|molecule.C21215]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AAB4|protein.P0AAB4]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-301`
- `QSPROTEOME:QS00195159`

## Notes

6*protein.P0AAB4
