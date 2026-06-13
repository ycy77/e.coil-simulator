---
entity_id: "complex.ecocyc.CPLX0-8544"
entity_type: "complex"
name: "KpLE2 phage-like element; 2,7-anhydro-N-acetylneuraminate hydratase"
source_database: "EcoCyc"
source_id: "CPLX0-8544"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# KpLE2 phage-like element; 2,7-anhydro-N-acetylneuraminate hydratase

`complex.ecocyc.CPLX0-8544`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8544`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P39353|protein.P39353]]

## Enriched Summary

NanY is a hydratase that is involved in the utilization of dehydrated forms of N-acetylneuraminate (Neu5Ac), specifically CPD-6182 (2,7-AN) and CPD-23638 (2,3-EN) . While wild-type E. coli K-12 is unable to utilize 2,7-AN or 2,3-EN as the sole source of carbon and energy, this appears to be due to transcriptional repression of nanXY by NanR. In a nanR mutant, 2,7-AN and 2,3-EN are utilized as sole carbon and energy sources . Conversely, were able to show growth of wild-type E. coli K-12 BW25113 on 2,7-AN. Of the putative substrates of NanY, NAD+, NADH, N-acetylneuraminate (Neu5Ac) and sialic acid 1,7 lactone affect the thermal stability and thus appear to bind to the enzyme. Although observed very little activity with Neu5Ac (with an apparent Km of 68.8 mM) and no activity with sialic acid 1,7 lactone in an in vitro assay, was able to show hydratase activity of NanY with both 2,7-AN and 2,3-EN in the presence of NAD+. The reaction mechanism is proposed to involve 4-keto intermediates and the transient formation of NADH , which has been confirmed for the homologous enzyme from Ruminococcus gnavus . A crystal structure of NanY in complex with NAD(H) has been solved at 1.35 Å resolution. The N-terminal domain shows a typical Rossmann fold . Respiration of a nanY mutant on various carbon sources was assessed using phenotype microarrays...

## Biological Role

Catalyzes RXN0-7367 (reaction.ecocyc.RXN0-7367), RXN0-7368 (reaction.ecocyc.RXN0-7368). Bound by NAD+ (molecule.C00003).

## Annotation

NanY is a hydratase that is involved in the utilization of dehydrated forms of N-acetylneuraminate (Neu5Ac), specifically CPD-6182 (2,7-AN) and CPD-23638 (2,3-EN) . While wild-type E. coli K-12 is unable to utilize 2,7-AN or 2,3-EN as the sole source of carbon and energy, this appears to be due to transcriptional repression of nanXY by NanR. In a nanR mutant, 2,7-AN and 2,3-EN are utilized as sole carbon and energy sources . Conversely, were able to show growth of wild-type E. coli K-12 BW25113 on 2,7-AN. Of the putative substrates of NanY, NAD+, NADH, N-acetylneuraminate (Neu5Ac) and sialic acid 1,7 lactone affect the thermal stability and thus appear to bind to the enzyme. Although observed very little activity with Neu5Ac (with an apparent Km of 68.8 mM) and no activity with sialic acid 1,7 lactone in an in vitro assay, was able to show hydratase activity of NanY with both 2,7-AN and 2,3-EN in the presence of NAD+. The reaction mechanism is proposed to involve 4-keto intermediates and the transient formation of NADH , which has been confirmed for the homologous enzyme from Ruminococcus gnavus . A crystal structure of NanY in complex with NAD(H) has been solved at 1.35 Å resolution. The N-terminal domain shows a typical Rossmann fold . Respiration of a nanY mutant on various carbon sources was assessed using phenotype microarrays. Metabolic activity on the carbon sources L-arabinose, D-arabinose, N-acetyl-D-glucosamine, D-trehalose, D-mannose, D-mannitol, D-fructose, α-D-glucose, maltose, α-D-lactose, N-acetyl-D-galactosamine, maltotriose, N-acetylneuraminate, β-D-allose, and D-galactonate-γ-lactone were reduced compared to E. coli BL21(DE3) . (Note: BL21(DE3) is not a K-12 strain and not the wild-type equivalent of the nanY mutant used.) NanY abundance is more than 2

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7367|reaction.ecocyc.RXN0-7367]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7368|reaction.ecocyc.RXN0-7368]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P39353|protein.P39353]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8544`
- `QSPROTEOME:QS00195925`

## Notes

2*protein.P39353
