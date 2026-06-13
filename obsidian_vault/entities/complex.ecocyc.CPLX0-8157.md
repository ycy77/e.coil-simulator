---
entity_id: "complex.ecocyc.CPLX0-8157"
entity_type: "complex"
name: "osmotically inducible peroxiredoxin OsmC"
source_database: "EcoCyc"
source_id: "CPLX0-8157"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# osmotically inducible peroxiredoxin OsmC

`complex.ecocyc.CPLX0-8157`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8157`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0C0L2|protein.P0C0L2]]

## Enriched Summary

OsmC from E. coli O157:H7 EDL933, which is 99% identical to the K-12 MG1622 protein, has been shown to have peroxidase activity with a strong preference for organic hydroperoxides . The catalytic activity involves oxidation of cysteine residues within the protein, which can subsequently be reduced by lipoylated proteins . The crystal structure of OsmC shows a domain-swapped dimer . Expression of osmC is induced before entry into stationary phase and by increased osmotic pressure . OsmC accumulates upon osmotic stress under both aerobic and anaerobic conditions and in the presence of the antifouling agent zosteric acid . Abundance of OsmC is decreased in a yfgM deletion strain . Mutations in H-NS lead to constitutive expression of osmC ; regulation of osmC expression by H-NS may be indirect . osmC mutants show increased sensitivity to oxidative stress and reduced viability during long-term stationary phase . Review: OsmC from E. coli O157:H7 EDL933, which is 99% identical to the K-12 MG1622 protein, has been shown to have peroxidase activity with a strong preference for organic hydroperoxides . The catalytic activity involves oxidation of cysteine residues within the protein, which can subsequently be reduced by lipoylated proteins . The crystal structure of OsmC shows a domain-swapped dimer...

## Biological Role

Catalyzes 1.11.1.15-RXN (reaction.ecocyc.1.11.1.15-RXN).

## Annotation

OsmC from E. coli O157:H7 EDL933, which is 99% identical to the K-12 MG1622 protein, has been shown to have peroxidase activity with a strong preference for organic hydroperoxides . The catalytic activity involves oxidation of cysteine residues within the protein, which can subsequently be reduced by lipoylated proteins . The crystal structure of OsmC shows a domain-swapped dimer . Expression of osmC is induced before entry into stationary phase and by increased osmotic pressure . OsmC accumulates upon osmotic stress under both aerobic and anaerobic conditions and in the presence of the antifouling agent zosteric acid . Abundance of OsmC is decreased in a yfgM deletion strain . Mutations in H-NS lead to constitutive expression of osmC ; regulation of osmC expression by H-NS may be indirect . osmC mutants show increased sensitivity to oxidative stress and reduced viability during long-term stationary phase . Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.1.11.1.15-RXN|reaction.ecocyc.1.11.1.15-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0C0L2|protein.P0C0L2]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8157`
- `QSPROTEOME:QS00190087`

## Notes

2*protein.P0C0L2
