---
entity_id: "protein.P75733"
entity_type: "protein"
name: "chiP"
source_database: "UniProt"
source_id: "P75733"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000305|PubMed:12192075}; Multi-pass membrane protein {ECO:0000305|PubMed:12192075}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "chiP ybfM b0681 JW0667"
---

# chiP

`protein.P75733`

## Static

- Type: `protein`
- Source: `UniProt:P75733`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000305|PubMed:12192075}; Multi-pass membrane protein {ECO:0000305|PubMed:12192075}.

## Enriched Summary

FUNCTION: Involved in the uptake of chitosugars. {ECO:0000305|PubMed:16857666, ECO:0000305|PubMed:19682266}. ChiP (formerly YbfM) is an outer membrane porin for chitooligosaccharides . Under standard growth conditions expression of chiP is negatively regulated by the RNA0-123, which acts by an antisense mechanism to silence chiP mRNA in vivo. ChiX RNA binds to a complementary region in the untranslated region of chiP mRNA that includes the Shine-Dalgarno sequence and destabilises the transcript. ChiX mediated regulation of chiP is dependent on the RNA binding protein EG10438-MONOMER Hfq . In the absence of chitosugars chiP expression is repressed by PD00266 NagC. Full induction of ChiP requires removal of both NagC mediated transcriptional repression and ChiX mediated translational repression . In the presence of chitosugars, antisense regulation of ChiX by the chitobiose operon mRNA (chb mRNA, the so-called 'trap mRNA') results in induction of chiP mRNA translation . The intergenic region (IGR) between the first and second gene of the chitobiose operon (chbBCARFG) possesses complementarity to the same region of ChiX that is used for targeting chiP mRNA. Growth of E. coli in chitobiose medium results in strongly reduced levels of ChiX and concomitant accumulation of chiP mRNA...

## Biological Role

Catalyzes TRANS-RXN-481 (reaction.ecocyc.TRANS-RXN-481).

## Annotation

FUNCTION: Involved in the uptake of chitosugars. {ECO:0000305|PubMed:16857666, ECO:0000305|PubMed:19682266}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-481|reaction.ecocyc.TRANS-RXN-481]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0681|gene.b0681]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75733`
- `KEGG:ecj:JW0667;eco:b0681;ecoc:C3026_03385;`
- `GeneID:945296;`
- `GO:GO:0006811; GO:0009279; GO:0015267; GO:0015288; GO:0015772; GO:0015774; GO:0046930; GO:0052778`

## Notes

Chitoporin (ChiP-III)
