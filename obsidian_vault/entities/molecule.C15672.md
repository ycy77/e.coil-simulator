---
entity_id: "molecule.C15672"
entity_type: "small_molecule"
name: "Heme O"
source_database: "KEGG"
source_id: "C15672"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Heme O"
---

# Heme O

`molecule.C15672`

## Static

- Type: `small_molecule`
- Source: `KEGG:C15672`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Heme O 'Heme' is usually understood as any tetrapyrrolic chelate of iron. The terms 'ferroheme' and 'ferriheme' refer to the Fe(II) and Fe(III) oxidation states in heme (even though Fe(IV) is found as a catalytic intermediate in some systems). HEME_A "Heme a" was first isolated in 1951 and shown to be the active component of the integral membrane metalloprotein EC-7.1.1.9 . The correct structure was published in 1975 . The immediate product of the initial heme biosynthesis pathways (by ferro-chelation of PROTOPORPHYRIN_IX) is Heme-b "heme b", whose PROTOHEME "ferrous form" is known as protoheme IX. HEME_A "Heme a" differs from heme b in that a methyl side chain at position 8 of the D ring is oxidized to a formyl group, and a hydroxyethylfarnesyl chain is attached to the vinyl side chain at position 2 of the A ring. It is synthesized from Heme-b via HEME_O by two enzymes - EC-2.5.1.141, and EC-1.17.99.9. The latter acts by two successive hydroxylations, with the first hydroxylation forming a short-lived Heme_I intermediate .

## Biological Role

Binds cytochrome bo3 ubiquinol:oxygen oxidoreductase (complex.ecocyc.CYT-O-UBIOX-CPLX).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Annotation

KEGG compound: Heme O

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Outgoing Edges (1)

- `binds` --> [[complex.ecocyc.CYT-O-UBIOX-CPLX|complex.ecocyc.CYT-O-UBIOX-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C15672`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
