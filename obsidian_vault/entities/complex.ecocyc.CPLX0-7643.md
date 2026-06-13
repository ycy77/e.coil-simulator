---
entity_id: "complex.ecocyc.CPLX0-7643"
entity_type: "complex"
name: "ketol-acid reductoisomerase (NADP+)"
source_database: "EcoCyc"
source_id: "CPLX0-7643"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "2-hydroxy-3-ketol-acid reductoisomerase"
  - "&alpha"
  - "-acetohydroxy acid isomeroreductase"
  - "acetohydroxy acid isomeroreductase"
  - "KARI"
---

# ketol-acid reductoisomerase (NADP+)

`complex.ecocyc.CPLX0-7643`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7643`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P05793|protein.P05793]]

## Enriched Summary

Ketol-acid reductoisomerase (IlvC, KARI) carries out two analogous reactions in the parallel biosynthetic pathways for the amino acids ILEUSYN-PWY isoleucine and VALSYN-PWY valine, converting 2-acetolactate to 2,3-dihydroxy-3-methylbutanoate (also known as 2,3-dihydroxy-isovalerate) and 2-aceto-2-hydroxy-butanoate to 2,3-dihydroxy-3-methylpentanoate (also known as 2,3-dihydroxy-3-methylvalerate) . The conversion of 2-acetolactate to 2,3-dihydroxy-3-methylbutanoate was long thought of as a two-step process, starting with the sequential binding of NADPH and acetolactate. In an isomerase reaction, acetolactate is converted to the intermediate compound 3-hydroxy-3-methyl-2-oxobutanoate; this 2-ketoacid is then reduced by the bound NADPH to generate the final product, 2,3-dihydroxy-3-methylbutanoate . The isomerase and reductase reactions occur at a single active site. In vitro, IlvC can act with reduced efficiency (typically 8% or less of normal) on a wide range of 2-keto and related substrates similar to the intermediate formed in the active site. The role of polar active site residues in the isomerase and reductase reactions has been investigated by site-directed mutagenesis. Certain mutations eliminate the isomerase activity of IlvC while retaining most of the reductase activity, but no mutations had the opposite effect...

## Biological Role

Catalyzes 2-DEHYDROPANTOATE-REDUCT-RXN (reaction.ecocyc.2-DEHYDROPANTOATE-REDUCT-RXN), ACETOLACTREDUCTOISOM-RXN (reaction.ecocyc.ACETOLACTREDUCTOISOM-RXN), ACETOOHBUTREDUCTOISOM-RXN (reaction.ecocyc.ACETOOHBUTREDUCTOISOM-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Ketol-acid reductoisomerase (IlvC, KARI) carries out two analogous reactions in the parallel biosynthetic pathways for the amino acids ILEUSYN-PWY isoleucine and VALSYN-PWY valine, converting 2-acetolactate to 2,3-dihydroxy-3-methylbutanoate (also known as 2,3-dihydroxy-isovalerate) and 2-aceto-2-hydroxy-butanoate to 2,3-dihydroxy-3-methylpentanoate (also known as 2,3-dihydroxy-3-methylvalerate) . The conversion of 2-acetolactate to 2,3-dihydroxy-3-methylbutanoate was long thought of as a two-step process, starting with the sequential binding of NADPH and acetolactate. In an isomerase reaction, acetolactate is converted to the intermediate compound 3-hydroxy-3-methyl-2-oxobutanoate; this 2-ketoacid is then reduced by the bound NADPH to generate the final product, 2,3-dihydroxy-3-methylbutanoate . The isomerase and reductase reactions occur at a single active site. In vitro, IlvC can act with reduced efficiency (typically 8% or less of normal) on a wide range of 2-keto and related substrates similar to the intermediate formed in the active site. The role of polar active site residues in the isomerase and reductase reactions has been investigated by site-directed mutagenesis. Certain mutations eliminate the isomerase activity of IlvC while retaining most of the reductase activity, but no mutations had the opposite effect. The equilibrium constant of the isomerase reaction highly favors 2-acetolactate. Together, these results suggest that no true intermediate is formed during the overall reaction, and that the reductase reaction occurs at the level of an isomerase transition state . The isomerisation step was further investigated, and a reaction mechanism involving a hydroxide that bridges the two Mg2+ ions in the active site abstracts a proton from the C2 OH group of the

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.2-DEHYDROPANTOATE-REDUCT-RXN|reaction.ecocyc.2-DEHYDROPANTOATE-REDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ACETOLACTREDUCTOISOM-RXN|reaction.ecocyc.ACETOLACTREDUCTOISOM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ACETOOHBUTREDUCTOISOM-RXN|reaction.ecocyc.ACETOOHBUTREDUCTOISOM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P05793|protein.P05793]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-7643`
- `QSPROTEOME:QS00181765`

## Notes

4*protein.P05793
