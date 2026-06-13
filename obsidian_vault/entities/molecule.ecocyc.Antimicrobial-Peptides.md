---
entity_id: "molecule.ecocyc.Antimicrobial-Peptides"
entity_type: "small_molecule"
name: "an antimicrobial peptide"
source_database: "EcoCyc"
source_id: "Antimicrobial-Peptides"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
---

# an antimicrobial peptide

`molecule.ecocyc.Antimicrobial-Peptides`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:Antimicrobial-Peptides`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

Antimicrobial peptides (AMPs) are a class of small peptides that widely exist in nature and form an important part of the innate immune system of different organisms. AMPs have a wide range of inhibitory effects against bacteria, fungi, parasites and viruses. While almost all AMPS are cationic, some anionic AMPs also exist. The AMPs have been classified based on several criteria, including their source, activity, structural characteristics, and amino acid composition. When classified based on sources, AMPs have been classidfied as originating from mammals, amphibians, microorganisms, and insects. When classified based on activity, AMPS are divided into antibacterial, antiviral, antifungal, antiparasitic, anti-human immunodeficiency virus (HIV), and anti-tumor peptides. When classified based on structure, AMPs have been divided into linear α-helical peptides, β-sheet peptides, linear extension structure, and both α-helix and β-sheet peptides. When classidied based on their composition, AMPs have been divided into proline-rich peptides, tryptophan- and arginine-rich antimicrobial peptides, histidine-rich peptides, and glycine-rich antimicrobial peptides. AMPs act by different mechanisms. The most common one is membrane-targeting, during which the AMPs generate a pore in the bacterial membrane. However, some AMPs enter the cell...

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Annotation

Antimicrobial peptides (AMPs) are a class of small peptides that widely exist in nature and form an important part of the innate immune system of different organisms. AMPs have a wide range of inhibitory effects against bacteria, fungi, parasites and viruses. While almost all AMPS are cationic, some anionic AMPs also exist. The AMPs have been classified based on several criteria, including their source, activity, structural characteristics, and amino acid composition. When classified based on sources, AMPs have been classidfied as originating from mammals, amphibians, microorganisms, and insects. When classified based on activity, AMPS are divided into antibacterial, antiviral, antifungal, antiparasitic, anti-human immunodeficiency virus (HIV), and anti-tumor peptides. When classified based on structure, AMPs have been divided into linear α-helical peptides, β-sheet peptides, linear extension structure, and both α-helix and β-sheet peptides. When classidied based on their composition, AMPs have been divided into proline-rich peptides, tryptophan- and arginine-rich antimicrobial peptides, histidine-rich peptides, and glycine-rich antimicrobial peptides. AMPs act by different mechanisms. The most common one is membrane-targeting, during which the AMPs generate a pore in the bacterial membrane. However, some AMPs enter the cell. where they can inhibit biosynthesis of proteins or nucleic acids, inhibit essential proteases, or interfere with cell division .

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-1594|reaction.ecocyc.TRANS-RXN-1594]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-1594|reaction.ecocyc.TRANS-RXN-1594]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.ABC-29-CPLX|complex.ecocyc.ABC-29-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `EcoCyc:Antimicrobial-Peptides`
