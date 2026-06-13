---
entity_id: "molecule.ecocyc.CPD-5242"
entity_type: "small_molecule"
name: "a tunicamycin"
source_database: "EcoCyc"
source_id: "CPD-5242"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "an N-[2-[3-acetylamino-4,5-dihydroxy-6-(hydroxymethyl) tetrahydropyran-2-yl]oxy-6-[2-[5-[(2,4-dioxo-1H-pyrimidin-1-yl)] -3,4-dihydroxy-tetrahydrofuran-2-yl]-2-hydroxy-ethyl]-4,5- dihydroxy-tetrahydropyran-3-yl]-5-methyl-hex-2-enamide"
  - "a mycospocidin"
---

# a tunicamycin

`molecule.ecocyc.CPD-5242`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:CPD-5242`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

CPD-5242 Tunicamycin is a mixture of nucleoside antibiotics targeting bacterial teichoic acid and peptidoglycan biosynthesis at the steps of EC-2.7.8.33, and EC-2.7.8.13, respectively. Tunicamycins cannot be used clinically since they are also acive against the eukaryotic enzyme EC-2.7.8.15, which is involved in an early step of protein N-glycosylation. The compounds bind specifically to the active site of the enzymes, blocking their activity and terminating the biosynthesis of the polymers at the first commited step . The first tunicamycin compound was originally isolated in 1957 under the name mycospocidin (it was eventually shown to be a tunicamycin ). A few years later more tunicamycin compounds were isolated from cultures of TAX-1079983, this time under the name tunicamycin, and initially described as anti-viral agents, although they were subsequently shown to be also active against yeasts, fungi and Gram-positive bacteria . Tunicamycins were subsequently isolated from TAX-1901 and TAX-1969, in which they accumulate to much higher concentrations. The process for tunicamycin preparation was patented 1980 with TAX-1079985 . All tunicamycins contain URACIL, N-acetyl-D-glucosamine, a unique 11-carbon 2-aminodialdose called CPD-19359, and a fatty acid linked to the amino group of the tunicamine...

## Annotation

CPD-5242 Tunicamycin is a mixture of nucleoside antibiotics targeting bacterial teichoic acid and peptidoglycan biosynthesis at the steps of EC-2.7.8.33, and EC-2.7.8.13, respectively. Tunicamycins cannot be used clinically since they are also acive against the eukaryotic enzyme EC-2.7.8.15, which is involved in an early step of protein N-glycosylation. The compounds bind specifically to the active site of the enzymes, blocking their activity and terminating the biosynthesis of the polymers at the first commited step . The first tunicamycin compound was originally isolated in 1957 under the name mycospocidin (it was eventually shown to be a tunicamycin ). A few years later more tunicamycin compounds were isolated from cultures of TAX-1079983, this time under the name tunicamycin, and initially described as anti-viral agents, although they were subsequently shown to be also active against yeasts, fungi and Gram-positive bacteria . Tunicamycins were subsequently isolated from TAX-1901 and TAX-1969, in which they accumulate to much higher concentrations. The process for tunicamycin preparation was patented 1980 with TAX-1079985 . All tunicamycins contain URACIL, N-acetyl-D-glucosamine, a unique 11-carbon 2-aminodialdose called CPD-19359, and a fatty acid linked to the amino group of the tunicamine. The various members of the tunicamycin group, all of which appear to have antimicrobial activity, differ only in the structure of their fatty acyl chain .

## Outgoing Edges (3)

- `represses` --> [[reaction.ecocyc.GLCNACPTRANS-RXN|reaction.ecocyc.GLCNACPTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PHOSNACMURPENTATRANS-RXN|reaction.ecocyc.PHOSNACMURPENTATRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-16650|reaction.ecocyc.RXN-16650]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `EcoCyc:CPD-5242`
- `SEED:cpd13403`
- `METANETX:MNXM88312`
- `LIGAND-CPD:C12063`
- `CHEBI:29699`
- `CHEMSPIDER:4938690`
- `PUBCHEM:6433557`
