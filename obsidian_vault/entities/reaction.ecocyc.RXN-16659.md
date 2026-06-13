---
entity_id: "reaction.ecocyc.RXN-16659"
entity_type: "reaction"
name: "peptidoglycan transpeptidase (Gram-negative bacteria)"
source_database: "EcoCyc"
source_id: "RXN-16659"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# peptidoglycan transpeptidase (Gram-negative bacteria)

`reaction.ecocyc.RXN-16659`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16659`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

Represents the formation of DD or 4-3 cross-links in the peptidoglycan (PG) of E. coli. D,D-transpeptidases (penicillin-binding proteins) attack the D-Ala4-D-Ala5 amide linkage of a donor stem pentapeptide with formation of an acyl-enzyme complex and release of D-alanine; the acyl-enzyme intermediate is deacylated via nucleophilic attack of an amino group in the meso-DAP side chain of an acceptor muropeptide (as shown in this reaction) or hydrolysed by water (see ). EcoCyc reaction equation: A-DONOR-PG-WITH-MESODAP-PENTAPEPTIDE + AN-ACCEPTOR-PG-WITH-MESODAP-TETRAPEPTIDE -> CPD0-2718 + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT. Represents the formation of DD or 4-3 cross-links in the peptidoglycan (PG) of E. coli. D,D-transpeptidases (penicillin-binding proteins) attack the D-Ala4-D-Ala5 amide linkage of a donor stem pentapeptide with formation of an acyl-enzyme complex and release of D-alanine; the acyl-enzyme intermediate is deacylated via nucleophilic attack of an amino group in the meso-DAP side chain of an acceptor muropeptide (as shown in this reaction) or hydrolysed by water (see ).

## Biological Role

Catalyzed by peptidoglycan glycosyltransferase / peptidoglycan DD-transpeptidase MrcB (complex.ecocyc.CPLX0-3951), peptidoglycan glycosyltransferase / peptidoglycan DD-transpeptidase MrcA (complex.ecocyc.CPLX0-7717), mrdA (protein.P0AD65), ftsI (protein.P0AD68). Substrates: a donor peptidoglycan with (L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanyl-D-alanine) pentapeptide (molecule.ecocyc.A-DONOR-PG-WITH-MESODAP-PENTAPEPTIDE), an acceptor peptidoglycan with (L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanine) tetrapeptide (molecule.ecocyc.AN-ACCEPTOR-PG-WITH-MESODAP-TETRAPEPTIDE). Products: D-Alanine (molecule.C00133), a peptidoglycan with D,D cross-links (meso-diaminoepimelate containing) (molecule.ecocyc.CPD0-2718).

## Enriched Pathways

- `ecocyc.PWY0-1586` peptidoglycan maturation (meso-diaminopimelate containing) (EcoCyc)

## Annotation

Represents the formation of DD or 4-3 cross-links in the peptidoglycan (PG) of E. coli. D,D-transpeptidases (penicillin-binding proteins) attack the D-Ala4-D-Ala5 amide linkage of a donor stem pentapeptide with formation of an acyl-enzyme complex and release of D-alanine; the acyl-enzyme intermediate is deacylated via nucleophilic attack of an amino group in the meso-DAP side chain of an acceptor muropeptide (as shown in this reaction) or hydrolysed by water (see ).

## Pathways

- `ecocyc.PWY0-1586` peptidoglycan maturation (meso-diaminopimelate containing) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (45)

- `activates` <-- [[protein.P0AB38|protein.P0AB38]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[protein.P45464|protein.P45464]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3951|complex.ecocyc.CPLX0-3951]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7717|complex.ecocyc.CPLX0-7717]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AD65|protein.P0AD65]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AD68|protein.P0AD68]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2718|molecule.ecocyc.CPD0-2718]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.A-DONOR-PG-WITH-MESODAP-PENTAPEPTIDE|molecule.ecocyc.A-DONOR-PG-WITH-MESODAP-PENTAPEPTIDE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.AN-ACCEPTOR-PG-WITH-MESODAP-TETRAPEPTIDE|molecule.ecocyc.AN-ACCEPTOR-PG-WITH-MESODAP-TETRAPEPTIDE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C06689|molecule.C06689]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-12294|molecule.ecocyc.CPD-12294]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-12301|molecule.ecocyc.CPD-12301]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-19296|molecule.ecocyc.CPD-19296]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-19952|molecule.ecocyc.CPD-19952]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-20701|molecule.ecocyc.CPD-20701]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-28124|molecule.ecocyc.CPD-28124]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9195|molecule.ecocyc.CPD-9195]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9220|molecule.ecocyc.CPD-9220]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9224|molecule.ecocyc.CPD-9224]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9227|molecule.ecocyc.CPD-9227]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9228|molecule.ecocyc.CPD-9228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9229|molecule.ecocyc.CPD-9229]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9231|molecule.ecocyc.CPD-9231]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9232|molecule.ecocyc.CPD-9232]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9235|molecule.ecocyc.CPD-9235]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2068|molecule.ecocyc.CPD0-2068]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2069|molecule.ecocyc.CPD0-2069]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2597|molecule.ecocyc.CPD0-2597]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2598|molecule.ecocyc.CPD0-2598]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2599|molecule.ecocyc.CPD0-2599]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2600|molecule.ecocyc.CPD0-2600]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2601|molecule.ecocyc.CPD0-2601]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2602|molecule.ecocyc.CPD0-2602]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2606|molecule.ecocyc.CPD0-2606]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2608|molecule.ecocyc.CPD0-2608]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2609|molecule.ecocyc.CPD0-2609]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2610|molecule.ecocyc.CPD0-2610]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2611|molecule.ecocyc.CPD0-2611]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2613|molecule.ecocyc.CPD0-2613]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2614|molecule.ecocyc.CPD0-2614]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2615|molecule.ecocyc.CPD0-2615]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.MOENOMYCIN|molecule.ecocyc.MOENOMYCIN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PENICILLIN-G|molecule.ecocyc.PENICILLIN-G]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[protein.P45955|protein.P45955]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-16659`

## Notes

A-DONOR-PG-WITH-MESODAP-PENTAPEPTIDE + AN-ACCEPTOR-PG-WITH-MESODAP-TETRAPEPTIDE -> CPD0-2718 + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT
