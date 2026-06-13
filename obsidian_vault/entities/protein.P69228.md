---
entity_id: "protein.P69228"
entity_type: "protein"
name: "baeR"
source_database: "UniProt"
source_id: "P69228"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "baeR b2079 JW2064"
---

# baeR

`protein.P69228`

## Static

- Type: `protein`
- Source: `UniProt:P69228`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system BaeS/BaeR which responds to envelope stress (PubMed:12354228). Activates expression of periplasmic chaperone spy in response to spheroplast formation, indole and P pili protein PapG overexpression (PubMed:12354228). Activates the mdtABCD (PubMed:12107133, PubMed:12107134) and probably the CRISPR-Cas casABCDE-ygbT-ygbF operon (PubMed:21255106). {ECO:0000269|PubMed:12107133, ECO:0000269|PubMed:12107134, ECO:0000269|PubMed:12354228, ECO:0000269|PubMed:21255106}. BaeR (bacterial adaptive response, response-regulator ) has been shown to regulate directly genes involved in drug resistance and indirectly appears to regulate genes involved in several cellular processes, such as flagellum biosynthesis, chemotaxis, and maltose transport . BaeR belongs to the BaeS/BaeR two-component system . Both genes, baeR, encoding the response regulator, and baeS, encoding the sensor kinase, are located at the end of the operon (mdtABCD-baeSR) regulated by BaeR . It has been suggested that BaeS senses envelope disorder . Indole and zinc have been used as inducers of this disorder. BaeR is the primary regulator of the ethanol stress response . Leblanc et al. identified two flavonoids and also sodium tungstate as novel inducers to BaeSR...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system BaeS/BaeR which responds to envelope stress (PubMed:12354228). Activates expression of periplasmic chaperone spy in response to spheroplast formation, indole and P pili protein PapG overexpression (PubMed:12354228). Activates the mdtABCD (PubMed:12107133, PubMed:12107134) and probably the CRISPR-Cas casABCDE-ygbT-ygbF operon (PubMed:21255106). {ECO:0000269|PubMed:12107133, ECO:0000269|PubMed:12107134, ECO:0000269|PubMed:12354228, ECO:0000269|PubMed:21255106}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (8)

- `activates` --> [[gene.b1743|gene.b1743]] `RegulonDB` `S` - regulator=BaeR; target=spy; function=+
- `activates` --> [[gene.b2074|gene.b2074]] `RegulonDB` `S` - regulator=BaeR; target=mdtA; function=+
- `activates` --> [[gene.b2075|gene.b2075]] `RegulonDB` `S` - regulator=BaeR; target=mdtB; function=+
- `activates` --> [[gene.b2076|gene.b2076]] `RegulonDB` `S` - regulator=BaeR; target=mdtC; function=+
- `activates` --> [[gene.b2077|gene.b2077]] `RegulonDB` `S` - regulator=BaeR; target=mdtD; function=+
- `activates` --> [[gene.b2078|gene.b2078]] `RegulonDB` `S` - regulator=BaeR; target=baeS; function=+
- `activates` --> [[gene.b2079|gene.b2079]] `RegulonDB` `S` - regulator=BaeR; target=baeR; function=+
- `activates` --> [[gene.b2470|gene.b2470]] `RegulonDB` `S` - regulator=BaeR; target=acrD; function=+

## Incoming Edges (1)

- `encodes` <-- [[gene.b2079|gene.b2079]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69228`
- `KEGG:ecj:JW2064;eco:b2079;ecoc:C3026_11690;`
- `GeneID:75056798;946605;`
- `GO:GO:0000156; GO:0000976; GO:0000987; GO:0005829; GO:0006355; GO:0032993; GO:0042802; GO:2000144; GO:2001023`

## Notes

Transcriptional regulatory protein BaeR
