---
entity_id: "protein.P0AC53"
entity_type: "protein"
name: "zwf"
source_database: "UniProt"
source_id: "P0AC53"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "zwf b1852 JW1841"
---

# zwf

`protein.P0AC53`

## Static

- Type: `protein`
- Source: `UniProt:P0AC53`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the oxidation of glucose 6-phosphate to 6-phosphogluconolactone. {ECO:0000255|HAMAP-Rule:MF_00966, ECO:0000269|PubMed:15113569, ECO:0000269|PubMed:17962566}.; FUNCTION: Probable source of extracellular death factor (EDF, sequence Asn-Asn-Trp-Asn-Asn, NNWNN) following processing and amidation. This pentapeptide stimulates cell death mediated by MazF (PubMed:17962566). Artificial peptides with altered sequence show that NNGNN, GNWNG and NWN no longer stimulate MazF's endoribonuclease activity; other peptides (NNGN, GNWMM, NNWNG, NNNWNNN) retain MazF-stimulating activity. NNWNN, NNGN, GNWMM and NNWNG prevent cognate antitoxin MazE from inhibiting MazF; although NNNWNNN stimulates MazF it does not do so in the presence of MazE. EDF also stimulates ChpB's endoribonuclease activity in vitro; in this case NWN partially stimulates ChpB, whereas NNGNN, GNWNN, NNWNG, GNWNG and NNNWNNN do not. Only the wild-type EDF peptide prevents cognate antitoxin ChpS from inhibiting ChpB (PubMed:21419338). {ECO:0000269|PubMed:17962566, ECO:0000269|PubMed:21419338}. Glucose-6-phosphate dehydrogenase (G6PDH) is the first enzyme of the PENTOSE-P-PWY and provides a large fraction of the NADPH needed for anabolism. The E. coli G6PDH shows a strong preference for NADP+ over NAD+...

## Biological Role

Catalyzes D-glucose-6-phosphate:NADP+ 1-oxidoreductase (reaction.R00835), beta-D-glucose-6-phosphate:NAD+ 1-oxidoreductase (reaction.R10907), GLU6PDEHYDROG-RXN (reaction.ecocyc.GLU6PDEHYDROG-RXN).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the oxidation of glucose 6-phosphate to 6-phosphogluconolactone. {ECO:0000255|HAMAP-Rule:MF_00966, ECO:0000269|PubMed:15113569, ECO:0000269|PubMed:17962566}.; FUNCTION: Probable source of extracellular death factor (EDF, sequence Asn-Asn-Trp-Asn-Asn, NNWNN) following processing and amidation. This pentapeptide stimulates cell death mediated by MazF (PubMed:17962566). Artificial peptides with altered sequence show that NNGNN, GNWNG and NWN no longer stimulate MazF's endoribonuclease activity; other peptides (NNGN, GNWMM, NNWNG, NNNWNNN) retain MazF-stimulating activity. NNWNN, NNGN, GNWMM and NNWNG prevent cognate antitoxin MazE from inhibiting MazF; although NNNWNNN stimulates MazF it does not do so in the presence of MazE. EDF also stimulates ChpB's endoribonuclease activity in vitro; in this case NWN partially stimulates ChpB, whereas NNGNN, GNWNN, NNWNG, GNWNG and NNNWNNN do not. Only the wild-type EDF peptide prevents cognate antitoxin ChpS from inhibiting ChpB (PubMed:21419338). {ECO:0000269|PubMed:17962566, ECO:0000269|PubMed:21419338}.

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00835|reaction.R00835]] `KEGG` `database` - via EC:1.1.1.49
- `catalyzes` --> [[reaction.R10907|reaction.R10907]] `KEGG` `database` - via EC:1.1.1.363
- `catalyzes` --> [[reaction.ecocyc.GLU6PDEHYDROG-RXN|reaction.ecocyc.GLU6PDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1852|gene.b1852]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC53`
- `KEGG:ecj:JW1841;eco:b1852;ecoc:C3026_10550;`
- `GeneID:86859388;946370;`
- `GO:GO:0004345; GO:0005829; GO:0006006; GO:0006098; GO:0009051; GO:0009372; GO:0042802; GO:0050661`
- `EC:1.1.1.49`

## Notes

Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49) [Cleaved into: Extracellular death factor (EDF)]
