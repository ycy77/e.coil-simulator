---
entity_id: "protein.P04816"
entity_type: "protein"
name: "livK"
source_database: "UniProt"
source_id: "P04816"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "livK b3458 JW3423"
---

# livK

`protein.P04816`

## Static

- Type: `protein`
- Source: `UniProt:P04816`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: This protein is a component of the leucine-specific transport system, which is one of the two periplasmic binding protein-dependent transport systems of the high-affinity transport of the branched-chain amino acids in E.coli. LivK is the periplasmic binding protein of the LS or leucine specific ABC transport system in E. coli K-12 . The LS system (LivKHMGF) is able to transport phenylanine and plays a physiologically relevant role in phenylalanine accumulation . The LS system transports both isomers of leucine . LivK is synthesized as a precursor; a 23 amino acid signal sequence is cleaved upon export to the periplasm . Purified LivK* binds L-leucine (apparent KD = 0.4 µM) and L-phenylalanine (apparent KD = 0.18 µM) but does not bind L-isoleucine or L-valine (KD > 1 mM) (LivK* denotes a protein that has been engineered with a StyI restriction site added at codon 124). The crystal structure of LivK in both the apo- and ligand-bound form has been determined at 1.5 and 1.8 A resolution . The protein consists of two domains connected by a 3-stranded hinge; in the closed form, ligands (phenylalanine and leucine) are bound in a cleft formed between the two domains; binding is stabilized by hydrogen bonds and van der Waals contacts.

## Biological Role

Component of leucine / L-phenylalanine ABC transporter (complex.ecocyc.ABC-304-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: This protein is a component of the leucine-specific transport system, which is one of the two periplasmic binding protein-dependent transport systems of the high-affinity transport of the branched-chain amino acids in E.coli.

## Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-304-CPLX|complex.ecocyc.ABC-304-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3458|gene.b3458]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P04816`
- `KEGG:ecj:JW3423;eco:b3458;ecoc:C3026_18730;`
- `GeneID:93778533;947964;`
- `GO:GO:0015803; GO:0015818; GO:0015820; GO:0015823; GO:0015829; GO:0016020; GO:0030288; GO:0055052; GO:0070728`

## Notes

Leucine-specific-binding protein (L-BP) (LS-BP)
