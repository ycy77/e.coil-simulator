---
entity_id: "complex.ecocyc.CPLX0-8123"
entity_type: "complex"
name: "6-carboxy-5,6,7,8-tetrahydropterin synthase"
source_database: "EcoCyc"
source_id: "CPLX0-8123"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 6-carboxy-5,6,7,8-tetrahydropterin synthase

`complex.ecocyc.CPLX0-8123`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8123`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P65870|protein.P65870]]

## Enriched Summary

QueD converts 7,8-dihydroneopterin triphosphate (H2NTP) to 6-carboxy-5,6,7,8-tetrahydropterin (CPH4). Because queuosine (Q) is the only deazapurine produced in E. coli, CPH4 is likely an intermediate in the pathway of queuosine biosynthesis . In initial in vitro studies under aerobic conditions, the enzyme was thought to catalyze 6-pyruvoyl tetrahydropterin synthesis . QueD belongs to the tunnel-fold superfamily of enzymes. Its mammalian homolog, 6-pyruvoyltetrahydropterin synthase (mPTPS), is required for the biosynthesis of 6R-L-erythro-5,6,7,8-tetrahydrobiopterin (BH4), an essential cofactor for many enzymes. The structural basis for the differing substrate specificities of these closely related enzymes is therefore of interest, and crystal structures of the enzyme have been solved . QueD consists of a hexamer of closely interacting trimers. Active site mutants have been analyzed for their activity ; two amino acid changes, W51M and F55L, can convert QueD to an enzyme with mammalian 6-pyruvoyltetrahydropterin synthase (PTPS) activity . A reaction mechanism has been proposed . Q-modified tRNA is absent when a ΔqueD strain is grown in defined minimal media but can be detected when this same strain is grown in minimal media supplemented with 10nM preQ0 or preQ1 . QueD converts 7,8-dihydroneopterin triphosphate (H2NTP) to 6-carboxy-5,6,7,8-tetrahydropterin (CPH4)...

## Biological Role

Catalyzes RXN0-5507 (reaction.ecocyc.RXN0-5507).

## Annotation

QueD converts 7,8-dihydroneopterin triphosphate (H2NTP) to 6-carboxy-5,6,7,8-tetrahydropterin (CPH4). Because queuosine (Q) is the only deazapurine produced in E. coli, CPH4 is likely an intermediate in the pathway of queuosine biosynthesis . In initial in vitro studies under aerobic conditions, the enzyme was thought to catalyze 6-pyruvoyl tetrahydropterin synthesis . QueD belongs to the tunnel-fold superfamily of enzymes. Its mammalian homolog, 6-pyruvoyltetrahydropterin synthase (mPTPS), is required for the biosynthesis of 6R-L-erythro-5,6,7,8-tetrahydrobiopterin (BH4), an essential cofactor for many enzymes. The structural basis for the differing substrate specificities of these closely related enzymes is therefore of interest, and crystal structures of the enzyme have been solved . QueD consists of a hexamer of closely interacting trimers. Active site mutants have been analyzed for their activity ; two amino acid changes, W51M and F55L, can convert QueD to an enzyme with mammalian 6-pyruvoyltetrahydropterin synthase (PTPS) activity . A reaction mechanism has been proposed . Q-modified tRNA is absent when a ΔqueD strain is grown in defined minimal media but can be detected when this same strain is grown in minimal media supplemented with 10nM preQ0 or preQ1 .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5507|reaction.ecocyc.RXN0-5507]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P65870|protein.P65870]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-8123`
- `QSPROTEOME:QS00188687`

## Notes

6*protein.P65870
