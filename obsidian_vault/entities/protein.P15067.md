---
entity_id: "protein.P15067"
entity_type: "protein"
name: "glgX"
source_database: "UniProt"
source_id: "P15067"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glgX glyX b3431 JW3394"
---

# glgX

`protein.P15067`

## Static

- Type: `protein`
- Source: `UniProt:P15067`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Removes maltotriose and maltotetraose chains that are attached by 1,6-alpha-linkage to the limit dextrin main chain, generating a debranched limit dextrin. Shows only very little activity with native glycogen. {ECO:0000269|PubMed:15687211, ECO:0000269|PubMed:779849, ECO:0000269|PubMed:8576033}. GlgX is a glycogen debranching enzyme. The purified enzyme shows only low activity toward Glycogens glycogen itself, but hydrolyzes 1,6-α-glucosidic linkages in CPD0-971 "limit dextrins" prepared from glycogen and amylopectin by treatment with phosphorylase and β-amylase . Recombinant GlgX efficiently hydrolyzes α-1,6-glucosidic linkages with degrees of polymerization of three or four glucose residues, and has very low or no activity with longer chains . The crystal structure of the enzyme has been determined at 2.25 Å resolution. The enzyme was found to be a monomer consisting of three major domains. A structural feature at the substrate binding groove suggests the basis of its unique specificity for G4 phosphorylase-limit dextrin and its discrimination toward substrates of varying length . GlgX has similarity to glycogen branching enzymes, glucan hydrolases and glucan transferases from other organisms . Overexpression of glgX leads to increased glycogen debranching activity...

## Biological Role

Catalyzes RXN0-5146 (reaction.ecocyc.RXN0-5146).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Removes maltotriose and maltotetraose chains that are attached by 1,6-alpha-linkage to the limit dextrin main chain, generating a debranched limit dextrin. Shows only very little activity with native glycogen. {ECO:0000269|PubMed:15687211, ECO:0000269|PubMed:779849, ECO:0000269|PubMed:8576033}.

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5146|reaction.ecocyc.RXN0-5146]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3431|gene.b3431]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15067`
- `KEGG:ecj:JW3394;eco:b3431;ecoc:C3026_18600;`
- `GeneID:75202276;947941;`
- `GO:GO:0004135; GO:0005980; GO:0006974; GO:0120549`
- `EC:3.2.1.196`

## Notes

Glycogen debranching enzyme (EC 3.2.1.196) (Glycogen operon protein GlgX) (Limit dextrin alpha-1,6-maltotetraose-hydrolase)
