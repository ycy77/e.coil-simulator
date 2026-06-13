---
entity_id: "protein.P0AE08"
entity_type: "protein"
name: "ahpC"
source_database: "UniProt"
source_id: "P0AE08"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:7499381}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ahpC b0605 JW0598"
---

# ahpC

`protein.P0AE08`

## Static

- Type: `protein`
- Source: `UniProt:P0AE08`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:7499381}.

## Enriched Summary

FUNCTION: Thiol-specific peroxidase that catalyzes the reduction of hydrogen peroxide and organic hydroperoxides to water and alcohols, respectively. Plays a role in cell protection against oxidative stress by detoxifying peroxides. Is the primary scavenger for endogenously generated hydrogen peroxides. {ECO:0000269|PubMed:11717276}. AhpC is the peroxidase component of alkyl hydroperoxide reductase belonging to the family of typical 2-Cys peroxiredoxins with two conserved redox-active cysteines. By similarity to the enzyme from Salmonella typhimurium, AhpC carries out the actual reduction of the hydroperoxide substrate. Under reduced conditions, AhpC forms a decameric ring composed of five homodimers that interact in a head-to-tail configuration, with intermolecular disulfide bonds between Cys47 of one subunit and Cys177 of the second subunit forming the active site . The C terminus is required for the dimer-to-decamer transition, anchors the AhpC-AhpF interaction, and undergoes redox-modulated structural rearrangements . A proteomics screen showed that AhpC interacts with ATP . AhpC has been found to interact with thioredoxin and the peptidyl-prolyl cis-trans isomerase PpiC . AhpC is 38% oxidatively modified in exponentially growing cells; this increases to 63.2% after hypochlorite treatment...

## Biological Role

Component of alkyl hydroperoxide reductase (complex.ecocyc.CPLX0-245).

## Annotation

FUNCTION: Thiol-specific peroxidase that catalyzes the reduction of hydrogen peroxide and organic hydroperoxides to water and alcohols, respectively. Plays a role in cell protection against oxidative stress by detoxifying peroxides. Is the primary scavenger for endogenously generated hydrogen peroxides. {ECO:0000269|PubMed:11717276}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-245|complex.ecocyc.CPLX0-245]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## Incoming Edges (1)

- `encodes` <-- [[gene.b0605|gene.b0605]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE08`
- `KEGG:ecj:JW0598;eco:b0605;`
- `GeneID:86863127;93776879;945225;`
- `GO:GO:0004601; GO:0005737; GO:0005829; GO:0006979; GO:0008379; GO:0009321; GO:0009970; GO:0016020; GO:0016684; GO:0019290; GO:0032843; GO:0033194; GO:0033195; GO:0042744; GO:0042802; GO:0045454; GO:0102039`
- `EC:1.11.1.26`

## Notes

Alkyl hydroperoxide reductase C (EC 1.11.1.26) (Alkyl hydroperoxide reductase protein C22) (Peroxiredoxin) (SCRP-23) (Sulfate starvation-induced protein 8) (SSI8) (Thioredoxin peroxidase)
