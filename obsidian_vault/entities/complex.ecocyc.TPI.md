---
entity_id: "complex.ecocyc.TPI"
entity_type: "complex"
name: "triose-phosphate isomerase"
source_database: "EcoCyc"
source_id: "TPI"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# triose-phosphate isomerase

`complex.ecocyc.TPI`

## Static

- Type: `complex`
- Source: `EcoCyc:TPI`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A858|protein.P0A858]]

## Enriched Summary

Triosephosphate isomerase (TpiA) catalyzes isomerization between glyceraldehyde 3-phosphate and didhydroxyacetone phosphate, a reaction involved in both glycolysis and gluconeogenesis. Triosephosphate isomerase (TIM) contains the TIM barrel fold, a structural motif that is also found in a variety of other unrelated enzymes. Recombinant E. coli TpiA has been compared with homologs from psychrophilic and thermophilic bacteria . Acetyl phosphate-dependent lysine acetylation of TpiA may affect its activity . Crystal structures of TpiA have been solved at 2.60 Å resolution ,1.85 Å resolution , and in complex with acetyl phosphate at 1.43 Å resolution . TpiA crystallizes as a dimer with two molecules in the asymmetric unit . The crystal structure of a chimeric E. coli-chicken triosephosphate isomerase has been solved at 2.80 Å resolution . TpiA is a known Immobilized Metal Affinity Chromatography (IMAC) binding protein and can be found as a contaminant in recombinant protein production . In early work, plasmid-borne tpiA was identified in the Clarke-Carbon clone bank , studied for gene dosage effects , and used in mapping studies . A tpiA mutant was unable to grow on glucose, lactate, or other carbon sources that require the activity of both the glycolysis and gluconeogenesis pathways . A tpiA knockout strain accumulates methylglyoxal during growth...

## Biological Role

Catalyzes TRIOSEPISOMERIZATION-RXN (reaction.ecocyc.TRIOSEPISOMERIZATION-RXN).

## Annotation

Triosephosphate isomerase (TpiA) catalyzes isomerization between glyceraldehyde 3-phosphate and didhydroxyacetone phosphate, a reaction involved in both glycolysis and gluconeogenesis. Triosephosphate isomerase (TIM) contains the TIM barrel fold, a structural motif that is also found in a variety of other unrelated enzymes. Recombinant E. coli TpiA has been compared with homologs from psychrophilic and thermophilic bacteria . Acetyl phosphate-dependent lysine acetylation of TpiA may affect its activity . Crystal structures of TpiA have been solved at 2.60 Å resolution ,1.85 Å resolution , and in complex with acetyl phosphate at 1.43 Å resolution . TpiA crystallizes as a dimer with two molecules in the asymmetric unit . The crystal structure of a chimeric E. coli-chicken triosephosphate isomerase has been solved at 2.80 Å resolution . TpiA is a known Immobilized Metal Affinity Chromatography (IMAC) binding protein and can be found as a contaminant in recombinant protein production . In early work, plasmid-borne tpiA was identified in the Clarke-Carbon clone bank , studied for gene dosage effects , and used in mapping studies . A tpiA mutant was unable to grow on glucose, lactate, or other carbon sources that require the activity of both the glycolysis and gluconeogenesis pathways . A tpiA knockout strain accumulates methylglyoxal during growth . TpiA activity is positively regulated by CsrA . Expression of tpiA is upregulated in a pgi mutant and downregulated in a pykF mutant . Addition of spermine reduces expression of TpiA . In a proteomic study of the E. coli metabolic response to acidic conditions, TpiA expression was constitutive in an ackA-pta deletion strain . tpiA mRNA and protein levels are increased in a Δrng mutant compared to wild type. RNase G cleaves the tp

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRIOSEPISOMERIZATION-RXN|reaction.ecocyc.TRIOSEPISOMERIZATION-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A858|protein.P0A858]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TPI`
- `QSPROTEOME:QS00165027`

## Notes

2*protein.P0A858
