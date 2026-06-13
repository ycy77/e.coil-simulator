---
entity_id: "protein.P00956"
entity_type: "protein"
name: "ileS"
source_database: "UniProt"
source_id: "P00956"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ileS ilvS b0026 JW0024"
---

# ileS

`protein.P00956`

## Static

- Type: `protein`
- Source: `UniProt:P00956`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the attachment of isoleucine to tRNA(Ile). As IleRS can inadvertently accommodate and process structurally similar amino acids such as valine, to avoid such errors it has two additional distinct tRNA(Ile)-dependent editing activities. One activity is designated as 'pretransfer' editing and involves the hydrolysis of activated Val-AMP. The other activity is designated 'posttransfer' editing and involves deacylation of mischarged Val-tRNA(Ile). {ECO:0000269|PubMed:10549284, ECO:0000269|PubMed:10889024, ECO:0000269|PubMed:11782529, ECO:0000269|PubMed:11864608, ECO:0000269|PubMed:12515858, ECO:0000269|PubMed:19557155, ECO:0000269|PubMed:3282306, ECO:0000269|PubMed:9554847}. Isoleucine-tRNA ligase (IleRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. IleRS belongs to the Class I aminoacyl tRNA synthetases . Specificity determinants within tRNAIle that are important for recognition by IleRS have been identified . The presence of the t6A modification at position 37 of tRNAIleGAU strongly enhances the aminoacylation rate by IleRS . Residues within IleRS that interact with tRNAIle have been identified . IleRS specifically acylates the 2'-OH and deacylates the 3'-OH of tRNAIle...

## Biological Role

Catalyzes ISOLEUCINE--TRNA-LIGASE-RXN (reaction.ecocyc.ISOLEUCINE--TRNA-LIGASE-RXN), RXN-23924 (reaction.ecocyc.RXN-23924), RXN-23944 (reaction.ecocyc.RXN-23944), RXN-23945 (reaction.ecocyc.RXN-23945). Bound by Zinc cation (molecule.C00038).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

FUNCTION: Catalyzes the attachment of isoleucine to tRNA(Ile). As IleRS can inadvertently accommodate and process structurally similar amino acids such as valine, to avoid such errors it has two additional distinct tRNA(Ile)-dependent editing activities. One activity is designated as 'pretransfer' editing and involves the hydrolysis of activated Val-AMP. The other activity is designated 'posttransfer' editing and involves deacylation of mischarged Val-tRNA(Ile). {ECO:0000269|PubMed:10549284, ECO:0000269|PubMed:10889024, ECO:0000269|PubMed:11782529, ECO:0000269|PubMed:11864608, ECO:0000269|PubMed:12515858, ECO:0000269|PubMed:19557155, ECO:0000269|PubMed:3282306, ECO:0000269|PubMed:9554847}.

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.ISOLEUCINE--TRNA-LIGASE-RXN|reaction.ecocyc.ISOLEUCINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-23924|reaction.ecocyc.RXN-23924]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-23944|reaction.ecocyc.RXN-23944]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-23945|reaction.ecocyc.RXN-23945]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0026|gene.b0026]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00956`
- `KEGG:ecj:JW0024;eco:b0026;ecoc:C3026_00125;`
- `GeneID:93777410;944761;`
- `GO:GO:0000049; GO:0002161; GO:0004822; GO:0005524; GO:0005829; GO:0006428; GO:0008270; GO:0046677`
- `EC:6.1.1.5`

## Notes

Isoleucine--tRNA ligase (EC 6.1.1.5) (Isoleucyl-tRNA synthetase) (IleRS)
