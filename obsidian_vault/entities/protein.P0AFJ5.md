---
entity_id: "protein.P0AFJ5"
entity_type: "protein"
name: "phoB"
source_database: "UniProt"
source_id: "P0AFJ5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "phoB b0399 JW0389"
---

# phoB

`protein.P0AFJ5`

## Static

- Type: `protein`
- Source: `UniProt:P0AFJ5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: This protein is a positive regulator for the phosphate regulon. Transcription of this operon is positively regulated by PhoB and PhoR when phosphate is limited. PhoB is a dual transcription regulator that activates expression of the Pho regulon in response to environmental Pi. The Pho regulon includes operons and genes whose products are involved in phosphorus uptake and metabolism . Expression of the periplasmic binding proteins for peptide transport, OppA and DppA, is repressed by PhoB . In a proteomic analysis under phosphate-limiting conditions, it was found that up to 400 proteins are differentially expressed . PhoB is also involved in bacterial virulence of pathogenic Escherichia coli . PhoB also regulates genes involved in the stimulation of cell persister resuscitation . Inhibition of phoB expression by CRISPRi enhanced cellular fitness under treatment with the antibiotic pyocyanin . PhoB is a response regulator and belongs to the two-component system PhoR/PhoB. Under phosphate-limited conditions, the inner membrane sensor kinase PhoR autophosphorylates. Subsequent transfer of the phosphate group to PhoB results in activation of PhoB . When phosphate is in excess, autophosphorylation of PhoR is inhibited and PhoB-P is dephosphorylated...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: This protein is a positive regulator for the phosphate regulon. Transcription of this operon is positively regulated by PhoB and PhoR when phosphate is limited.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (57)

- `activates` --> [[gene.b0241|gene.b0241]] `RegulonDB` `C` - regulator=PhoB; target=phoE; function=+
- `activates` --> [[gene.b0383|gene.b0383]] `RegulonDB` `C` - regulator=PhoB; target=phoA; function=+
- `activates` --> [[gene.b0384|gene.b0384]] `RegulonDB` `C` - regulator=PhoB; target=psiF; function=+
- `activates` --> [[gene.b0399|gene.b0399]] `RegulonDB` `C` - regulator=PhoB; target=phoB; function=+
- `activates` --> [[gene.b0400|gene.b0400]] `RegulonDB` `C` - regulator=PhoB; target=phoR; function=+
- `activates` --> [[gene.b0570|gene.b0570]] `RegulonDB` `C` - regulator=PhoB; target=cusS; function=+
- `activates` --> [[gene.b0571|gene.b0571]] `RegulonDB` `C` - regulator=PhoB; target=cusR; function=+
- `activates` --> [[gene.b0572|gene.b0572]] `RegulonDB` `C` - regulator=PhoB; target=cusC; function=+
- `activates` --> [[gene.b0573|gene.b0573]] `RegulonDB` `C` - regulator=PhoB; target=cusF; function=+
- `activates` --> [[gene.b0574|gene.b0574]] `RegulonDB` `C` - regulator=PhoB; target=cusB; function=+
- `activates` --> [[gene.b0575|gene.b0575]] `RegulonDB` `C` - regulator=PhoB; target=cusA; function=+
- `activates` --> [[gene.b1020|gene.b1020]] `RegulonDB` `C` - regulator=PhoB; target=phoH; function=+
- `activates` --> [[gene.b1540|gene.b1540]] `RegulonDB` `S` - regulator=PhoB; target=rspR; function=+
- `activates` --> [[gene.b1597|gene.b1597]] `RegulonDB` `S` - regulator=PhoB; target=asr; function=+
- `activates` --> [[gene.b1782|gene.b1782]] `RegulonDB` `S` - regulator=PhoB; target=mipA; function=+
- `activates` --> [[gene.b1788|gene.b1788]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1970|gene.b1970]] `RegulonDB` `S` - regulator=PhoB; target=hiuH; function=+
- `activates` --> [[gene.b1971|gene.b1971]] `RegulonDB` `S` - regulator=PhoB; target=msrP; function=+
- `activates` --> [[gene.b1972|gene.b1972]] `RegulonDB` `S` - regulator=PhoB; target=msrQ; function=+
- `activates` --> [[gene.b1982|gene.b1982]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2063|gene.b2063]] `RegulonDB` `S` - regulator=PhoB; target=yegH; function=+
- `activates` --> [[gene.b3449|gene.b3449]] `RegulonDB` `S` - regulator=PhoB; target=ugpQ; function=-+
- `activates` --> [[gene.b3450|gene.b3450]] `RegulonDB` `S` - regulator=PhoB; target=ugpC; function=-+
- `activates` --> [[gene.b3451|gene.b3451]] `RegulonDB` `S` - regulator=PhoB; target=ugpE; function=-+
- `activates` --> [[gene.b3452|gene.b3452]] `RegulonDB` `S` - regulator=PhoB; target=ugpA; function=-+
- `activates` --> [[gene.b3453|gene.b3453]] `RegulonDB|EcoCyc` `C` - regulator=PhoB; target=ugpB; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3521|gene.b3521]] `RegulonDB` `S` - regulator=PhoB; target=rcdB; function=+
- `activates` --> [[gene.b3725|gene.b3725]] `RegulonDB` `C` - regulator=PhoB; target=pstB; function=+
- `activates` --> [[gene.b3726|gene.b3726]] `RegulonDB` `C` - regulator=PhoB; target=pstA; function=+
- `activates` --> [[gene.b3727|gene.b3727]] `RegulonDB` `C` - regulator=PhoB; target=pstC; function=+
- `activates` --> [[gene.b3728|gene.b3728]] `RegulonDB` `C` - regulator=PhoB; target=pstS; function=+
- `activates` --> [[gene.b4030|gene.b4030]] `RegulonDB` `S` - regulator=PhoB; target=psiE; function=+
- `activates` --> [[gene.b4092|gene.b4092]] `RegulonDB` `S` - regulator=PhoB; target=phnP; function=+
- `activates` --> [[gene.b4093|gene.b4093]] `RegulonDB` `S` - regulator=PhoB; target=phnO; function=+
- `activates` --> [[gene.b4094|gene.b4094]] `RegulonDB` `S` - regulator=PhoB; target=phnN; function=+
- `activates` --> [[gene.b4095|gene.b4095]] `RegulonDB` `S` - regulator=PhoB; target=phnM; function=+
- `activates` --> [[gene.b4096|gene.b4096]] `RegulonDB` `S` - regulator=PhoB; target=phnL; function=+
- `activates` --> [[gene.b4097|gene.b4097]] `RegulonDB` `S` - regulator=PhoB; target=phnK; function=+
- `activates` --> [[gene.b4098|gene.b4098]] `RegulonDB` `S` - regulator=PhoB; target=phnJ; function=+
- `activates` --> [[gene.b4099|gene.b4099]] `RegulonDB` `S` - regulator=PhoB; target=phnI; function=+
- `activates` --> [[gene.b4100|gene.b4100]] `RegulonDB` `S` - regulator=PhoB; target=phnH; function=+
- `activates` --> [[gene.b4101|gene.b4101]] `RegulonDB` `S` - regulator=PhoB; target=phnG; function=+
- `activates` --> [[gene.b4102|gene.b4102]] `RegulonDB` `S` - regulator=PhoB; target=phnF; function=+
- `activates` --> [[gene.b4105|gene.b4105]] `RegulonDB` `S` - regulator=PhoB; target=phnD; function=+
- `activates` --> [[gene.b4106|gene.b4106]] `RegulonDB|EcoCyc` `S` - regulator=PhoB; target=phnC; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4554|gene.b4554]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0330|gene.b0330]] `RegulonDB` `S` - regulator=PhoB; target=prpR; function=-
- `represses` --> [[gene.b0397|gene.b0397]] `RegulonDB` `C` - regulator=PhoB; target=sbcC; function=-
- `represses` --> [[gene.b0398|gene.b0398]] `RegulonDB` `C` - regulator=PhoB; target=sbcD; function=-
- `represses` --> [[gene.b1002|gene.b1002]] `RegulonDB|EcoCyc` `S` - regulator=PhoB; target=agp; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1384|gene.b1384]] `RegulonDB|EcoCyc` `S` - regulator=PhoB; target=feaR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1850|gene.b1850]] `RegulonDB` `S` - regulator=PhoB; target=eda; function=-
- `represses` --> [[gene.b3449|gene.b3449]] `RegulonDB` `S` - regulator=PhoB; target=ugpQ; function=-+
- `represses` --> [[gene.b3450|gene.b3450]] `RegulonDB` `S` - regulator=PhoB; target=ugpC; function=-+
- `represses` --> [[gene.b3451|gene.b3451]] `RegulonDB` `S` - regulator=PhoB; target=ugpE; function=-+
- `represses` --> [[gene.b3452|gene.b3452]] `RegulonDB` `S` - regulator=PhoB; target=ugpA; function=-+
- `represses` --> [[gene.b3453|gene.b3453]] `RegulonDB` `C` - regulator=PhoB; target=ugpB; function=-+

## Incoming Edges (1)

- `encodes` <-- [[gene.b0399|gene.b0399]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFJ5`
- `KEGG:ecj:JW0389;eco:b0399;ecoc:C3026_01940;`
- `GeneID:86862944;93777061;945046;`
- `GO:GO:0000156; GO:0000976; GO:0001108; GO:0005829; GO:0006355; GO:0006817; GO:0032993; GO:0042802; GO:2000142`

## Notes

Phosphate regulon transcriptional regulatory protein PhoB
