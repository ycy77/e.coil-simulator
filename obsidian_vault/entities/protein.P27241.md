---
entity_id: "protein.P27241"
entity_type: "protein"
name: "waaZ"
source_database: "UniProt"
source_id: "P27241"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:12591884}. Note=When overexpressed, a significant amount is also located in the membrane fraction. {ECO:0000269|PubMed:12591884}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "waaZ rfaZ b3624 JW3599"
---

# waaZ

`protein.P27241`

## Static

- Type: `protein`
- Source: `UniProt:P27241`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:12591884}. Note=When overexpressed, a significant amount is also located in the membrane fraction. {ECO:0000269|PubMed:12591884}.

## Enriched Summary

FUNCTION: Involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:12591884). Required for the addition of 3-deoxy-D-manno-oct-2-ulosonic acid III (KdoIII) to the KdoII residue of the inner lipopolysaccharide core (PubMed:12591884). May also play a role in a lipooligosaccharide (LOS) biosynthesis pathway (PubMed:1385388). {ECO:0000269|PubMed:12591884, ECO:0000269|PubMed:1385388}. The lipopolysaccharide of E. coli K-12 consists of two major components: the hydrophobic lipid A moiety inserted into the outer membrane and the phosphorylated core oligosaccharide . E. coli K-12 does not produce O antigen to attach to the LPS core due to a defect in the rfb gene cluster which can be complemented with genes from a second, independent rfb mutant to produce an O16 type O antigen . E. coli K-12 may have two major pathways for LPS biosynthesis. One generates LPS cores suitable for O antigen attachment, and a second generates lipooligosaccharides (LOS) with modifications to the core structure which prevent O antigen attachment . WaaZ is involved in the nonstoichiometric addition of 3-deoxy-D-manno-oct-2-ulosonic acid III (KDOIII) to the KDOII residue of the inner lipopolysaccharide core . WaaZ could play a role in an LOS biosynthesis pathway, because waaZ mutants do not produce certain unsubstituted core bands...

## Biological Role

Catalyzes (KDO)3-lipid IVA (2->4) 3-deoxy-D-manno-octulosonic acid transferase (reaction.ecocyc.RXN-11326).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:12591884). Required for the addition of 3-deoxy-D-manno-oct-2-ulosonic acid III (KdoIII) to the KdoII residue of the inner lipopolysaccharide core (PubMed:12591884). May also play a role in a lipooligosaccharide (LOS) biosynthesis pathway (PubMed:1385388). {ECO:0000269|PubMed:12591884, ECO:0000269|PubMed:1385388}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11326|reaction.ecocyc.RXN-11326]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3624|gene.b3624]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27241`
- `KEGG:ecj:JW3599;eco:b3624;ecoc:C3026_19645;`
- `GeneID:948146;`
- `GO:GO:0005737; GO:0005886; GO:0009244; GO:0043842`
- `EC:2.4.99.15`

## Notes

Probable 3-deoxy-manno-octulosonic acid transferase (Kdo transferase) (EC 2.4.99.15) (Lipopolysaccharide core biosynthesis protein WaaZ)
