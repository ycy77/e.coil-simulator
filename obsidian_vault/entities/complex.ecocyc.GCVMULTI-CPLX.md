---
entity_id: "complex.ecocyc.GCVMULTI-CPLX"
entity_type: "complex"
name: "glycine cleavage system"
source_database: "EcoCyc"
source_id: "GCVMULTI-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glycine cleavage system

`complex.ecocyc.GCVMULTI-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GCVMULTI-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.E3-CPLX|complex.ecocyc.E3-CPLX]], [[complex.ecocyc.GCVP-CPLX|complex.ecocyc.GCVP-CPLX]], [[protein.P0A6T9|protein.P0A6T9]], [[protein.P27248|protein.P27248]]

## Enriched Summary

The glycine-cleavage system (GCV) is a multienzyme complex that catalyzes the reversible oxidation of glycine, yielding carbon dioxide, ammonia, 5,10-methylenetetrahydrofolate and a reduced pyridine nucleotide. Tetrahydrofolate serves as a recipient for one-carbon units generated during glycine cleavage to form the methylene group. The GCV system consists of four protein components, the P protein, H protein, T protein, and L protein. P protein catalyzes the pyridoxal phosphate-dependent liberation of CO2 from glycine, leaving a methylamine moiety. The methylamine moiety is transferred to the lipoic acid group of the H protein, which is bound to the P protein prior to decarboxylation of glycine. The T protein catalyzes the release of NH3 from the methylamine group and transfers the remaining C1 unit to THF, forming 5,10-mTHF. The L protein then oxidizes the lipoic acid component of the H protein and transfers the electrons to NAD+, forming NADH . Mutations that result in an enzymatic deficiency in the GCV enzyme system (gcvT, gcvH, and gcvP) do not result in auxotrophy. Mutations that result in an enzymatic deficiency in both the serine pathway and the GCV enzyme system can no longer use glycine as a serine source . Mutants that overproduce the GCV enzyme complex are partial glycine auxotrophs due to rapid glycine catabolism....

## Biological Role

Catalyzes GCVMULTI-RXN (reaction.ecocyc.GCVMULTI-RXN). Bound by (R)-Lipoate (molecule.C16241).

## Annotation

The glycine-cleavage system (GCV) is a multienzyme complex that catalyzes the reversible oxidation of glycine, yielding carbon dioxide, ammonia, 5,10-methylenetetrahydrofolate and a reduced pyridine nucleotide. Tetrahydrofolate serves as a recipient for one-carbon units generated during glycine cleavage to form the methylene group. The GCV system consists of four protein components, the P protein, H protein, T protein, and L protein. P protein catalyzes the pyridoxal phosphate-dependent liberation of CO2 from glycine, leaving a methylamine moiety. The methylamine moiety is transferred to the lipoic acid group of the H protein, which is bound to the P protein prior to decarboxylation of glycine. The T protein catalyzes the release of NH3 from the methylamine group and transfers the remaining C1 unit to THF, forming 5,10-mTHF. The L protein then oxidizes the lipoic acid component of the H protein and transfers the electrons to NAD+, forming NADH . Mutations that result in an enzymatic deficiency in the GCV enzyme system (gcvT, gcvH, and gcvP) do not result in auxotrophy. Mutations that result in an enzymatic deficiency in both the serine pathway and the GCV enzyme system can no longer use glycine as a serine source . Mutants that overproduce the GCV enzyme complex are partial glycine auxotrophs due to rapid glycine catabolism. . One of the four subunits, lipoamide dehydrogenase (E3), is shared with pyruvate dehydrogenase and 2-oxoglutarate dehydrogenase . This topic has been reviewed in .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GCVMULTI-RXN|reaction.ecocyc.GCVMULTI-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (7)

- `binds` <-- [[molecule.C16241|molecule.C16241]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[complex.ecocyc.E3-CPLX|complex.ecocyc.E3-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.GCVP-CPLX|complex.ecocyc.GCVP-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P0A6T9|protein.P0A6T9]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0A9P0|protein.P0A9P0]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P27248|protein.P27248]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P33195|protein.P33195]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:GCVMULTI-CPLX`
- `QSPROTEOME:QS00196451`

## Notes

1*complex.ecocyc.E3-CPLX|1*complex.ecocyc.GCVP-CPLX|1*protein.P0A6T9|1*protein.P27248
