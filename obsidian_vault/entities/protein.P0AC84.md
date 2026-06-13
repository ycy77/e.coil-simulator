---
entity_id: "protein.P0AC84"
entity_type: "protein"
name: "gloB"
source_database: "UniProt"
source_id: "P0AC84"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gloB yafR b0212 JW0202"
---

# gloB

`protein.P0AC84`

## Static

- Type: `protein`
- Source: `UniProt:P0AC84`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Type II glyoxalase that catalyzes the hydrolysis of (R)-S-lactoylglutathione to (R)-lactate and glutathione (PubMed:17196158, PubMed:25670698). Is more efficient than the isozyme GloC, and plays a major contribution to methylglyoxal (MG) detoxification in E.coli (PubMed:25670698). The two isoenzymes have additive effects and ensure maximal MG degradation (PubMed:25670698). {ECO:0000269|PubMed:17196158, ECO:0000269|PubMed:25670698}. Glyoxalase II catalyzes the second of two sequential reactions in the conversion of methylglyoxal to D-lactate . The enzyme contains ~1.7 molecules of Zn2+ per active monomer. Co2+ and Mn2+ can substitute for Zn2+, but Ni2+ can not . A gloB null mutant accumulates S-lactoylglutathione upon methylglyoxal exposure and has a depleted glutathione pool. This leads to activation of the KefB potassium efflux system, which causes cytoplasmic acidification and protection against methylglyoxal toxicity. Conversely, overexpression of gloB leads to depletion of S-lactoylglutathione and increased sensitivity to methylglyoxal . gloB shows differential codon adaptation, resulting in differential translation efficiency signatures, in thermophilic microbes. It was therefore predicted to play a role in the heat shock response. A gloB deletion mutant was shown to be more sensitive than wild-type specifically to heat shock, but not other stresses...

## Biological Role

Catalyzes (R)-S-lactoylglutathione hydrolase (reaction.R01736), GLYOXII-RXN (reaction.ecocyc.GLYOXII-RXN). Bound by Zinc cation (molecule.C00038).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Type II glyoxalase that catalyzes the hydrolysis of (R)-S-lactoylglutathione to (R)-lactate and glutathione (PubMed:17196158, PubMed:25670698). Is more efficient than the isozyme GloC, and plays a major contribution to methylglyoxal (MG) detoxification in E.coli (PubMed:25670698). The two isoenzymes have additive effects and ensure maximal MG degradation (PubMed:25670698). {ECO:0000269|PubMed:17196158, ECO:0000269|PubMed:25670698}.

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01736|reaction.R01736]] `KEGG` `database` - via EC:3.1.2.6
- `catalyzes` --> [[reaction.ecocyc.GLYOXII-RXN|reaction.ecocyc.GLYOXII-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0212|gene.b0212]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC84`
- `KEGG:ecj:JW0202;eco:b0212;ecoc:C3026_00990;`
- `GeneID:944902;`
- `GO:GO:0004416; GO:0008270; GO:0009408; GO:0019243`
- `EC:3.1.2.6`

## Notes

Hydroxyacylglutathione hydrolase GloB (EC 3.1.2.6) (Glyoxalase II) (Glx II)
